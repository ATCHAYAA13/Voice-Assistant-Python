from tkinter import *
import customtkinter as ctk
import speech_recognition as sr
from PIL import Image, ImageTk
from packaging import version
from tkinter import scrolledtext
import tkinter as tk
import smtplib
import datetime
import pyttsx3
import webbrowser
import requests
import os
import time
import shutil


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()

def wish():
    print("Wishing.")
    time = int(datetime.datetime.now().hour)
    global uname,asname
    if time>= 0 and time<12:
        speak("Good Morning ")

    elif time<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening !")

    
    speak("I am your Voice Assistant ,")
    
    print("I am your Voice Assistant,")
    speak("How can I assist you today,")
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)

def takeCommand():
    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:        
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")
        

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command


def getWeather(city_name):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name 
    response = requests.get(url)
    x = response.json()

    #If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp-=273 
        pressure = y["pressure"]
        humidity = y["humidity"]
        desc = x["weather"]
        description = desc[0]["description"]
        info=(" Temperature is " +str(round(temp,2))+"°C"+"\n atmospheric pressure (hPa) is"+str(pressure) +"\n humidity is " +str(humidity)+"%" +"\n description is " +str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
    else:
        speak(" City Not Found ")



def startRecognition():
    if __name__ == '__main__':
        uname=''
        os.system('cls')
        wish()
        getName()
        print(uname)

    while True:
        command = takeCommand().lower()
        print(command)
        
                
        if 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)
            
        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" +command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
        
        elif "who are you" in command:
            speak("I am your virtual assistant.")

        elif "change my name to" in command:
            speak("What would you like me to call you,  ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)
            
            
        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)

        elif 'open youtube' in command:
            speak("Here you go, the Youtube is opening\n")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("google.com")
        
        elif 'exit' in command:
            speak("Thanks for giving me your time")
            exit()

        elif "weather" in command:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeCommand()
            getWeather(cityName)

        elif "don't listen" in command or "stop listening" in command:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "write a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('file1.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        else:
            speak("Sorry, I am not able to understand you")



     

#Creating the main window 
root = ctk.CTk() 
root.title("Voice Assistant")
root.iconbitmap("D:\ATCHAYAA THINGAL\Projects\Oasis Infotech\Voice Assistant\Voiceassistant icon.ico")
root.geometry('500x650')

#image
vc_image = ImageTk.PhotoImage(Image.open("D:\ATCHAYAA THINGAL\Projects\Oasis Infotech\Voice Assistant\Voice assistant image.jpg"))
vc1 = Label(root, image=vc_image, bd=0)
vc1.pack(pady=20)


#Button to convert PDF to Audio form
# Create a button to start speech recognition
start_button = ctk.CTkButton(root, text="Start Recognition",fg_color="#085454",hover_color="#FFB30D",corner_radius=20,command=startRecognition)
start_button.pack(pady=10)

showCommand=StringVar()



#Runs the window till it is closed
root.mainloop()