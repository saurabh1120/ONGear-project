import sys
from cv2 import data
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import cv2
import random
import pywhatkit as kit
import smtplib
from requests import get
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
import numpy as np
import pyautogui as p


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" I can recognise you sir, face verification successful ")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak(" I recognise you sir, face verification successful ")
        speak("Good Afternoon!")   

    else:
        speak(" I recognise you sir, face verification successful  ")
        speak("Good Evening!")  
    
    speak("I am genie  . Please tell me how can i do for you ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir your commamd: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def TaskExecution():
#      p.press("esc")
#      speak("verification successful")
#      speak("welcome back sir, good to see you")
#      wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saurabhsinha1850@gmail.com', 'Saurabh321!!')
    server.sendmail('saurabhsinha1850@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
    wishMe()

    # if 1:     
    while True:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who is' in query:
            speak('ok sir i am looking for it ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(" i got the result sir ")
            print(results)
            speak(results)

        
        elif 'wikipedia' in query:
            speak('ok sir i am looking for it ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open notepad" in query:
            speak("ok sir")
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            speak("ok sir")
            os.system("start cmd")
        

        elif "open camera" in query:
            speak("ok sir")
            cap =cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "who are you"  in query:
            speak("i am your personal assistant genie")

        elif "who made you" in query:
            speak("you made me sir")
        
        elif "you know me" in query:
            speak("yes sir")
            speak("you are my master, i can do anything for you sir, command me sir")

        elif 'open youtube' in query:
            speak("ok sir")
            webbrowser.open("www.youtube.com")
            

        elif 'search' in query:
            speak("ok sir")
            speak("what should i search for you ")
            g=takeCommand().lower()
            webbrowser.open(f"{g}")
            speak(g)
    
        elif 'stack overflow' in query:
            speak("ok sir")
            webbrowser.open("www.stackoverflow.com")   
        
        elif 'open facebook' in query:
            speak("ok sir")
            webbrowser.open("www.facebook.com") 
        


        elif 'play music' in query:
            speak("ok sir")
            music_dir = 'C:\\Users\\saurabh\\Desktop\\Song 1'
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            print("\n",songs)    
            os.startfile(os.path.join(music_dir, rd))
        
        
        elif 'stop music' in query:
            speak("ok sir")


        elif 'change' in query:
            speak("ok sir")
            music_dir = 'C:\\Users\\saurabh\\Desktop\\Song 1'
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            print("\n",songs)    
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip =get("https://api.ipify.org").text
            speak(f" sir your IP Address is {ip}")
            print(ip)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, current time is {strTime}")

        elif 'code' in query:
            speak("ok sir")
            codePath = "C:\\Users\\saurabh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        
        elif "send message" in query:
            speak("ok sir")
            kit.sendwhatmsg("+918839868432","this message is comming from ginie",2,25)
            # speak("what should i search for you ")
            # w=takeCommand().lower()
            # webbrowser.open(f"{w}")
        
        # elif 'weather' in query:
            
        elif "weather in bangalore" in query:
            speak("ok sir")
            sch="weather in bangalore"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")
        

        elif "weather in delhi" in query:
            speak("ok sir")
            sch="weather in delhi"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")


        elif "weather in chhattisgarh" in query:
            speak("ok sir")
            sch="weather in chhattisgarh"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")
        

        elif "weather in bihar" in query:
            speak("ok sir")
            sch="weather in bihar"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")

        elif "weather in mumbai" in query:
            speak("ok sir")
            sch="weather in mumbai"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")
        
        elif "weather in gujarat" in query:
            speak("ok sir")
            sch="weather in gujarat"
            url=(f"https://www.google.com/search?q={sch}")
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {sch} is {temp}")


        elif "play video youtube" in query:
            speak("ok sir")
            speak("what should i search in youtube ")
            y=takeCommand().lower()
            kit.playonyt(f"{y}")
            speak(y)
        

        elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                to = "saurabhsinha1850@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email") 


        elif 'rest' in query:
            speak("thankyou sir, have a good day . ")
            sys.exit()


# if __name__ == "__main__":
        

#     recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
#     recognizer.read('trainer/trainer.yml')   #load trained model
#     cascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

#     font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


#     id = 2 #number of persons you want to Recognize


#     names = ['','saurabh']  #names, leave first empty bcz counter starts from 0


#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
#     cam.set(3, 640) # set video FrameWidht
#     cam.set(4, 480) # set video FrameHeight

#     # Define min window size to be recognized as a face
#     minW = 0.1*cam.get(3)
#     minH = 0.1*cam.get(4)

#     # flag = True

#     while True:

#         ret, img =cam.read() #read the frames using the above created object

#         converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

#         faces = faceCascade.detectMultiScale( 
#             converted_image,
#             scaleFactor = 1.2,
#             minNeighbors = 5,
#             minSize = (int(minW), int(minH)),
#         )

#         for(x,y,w,h) in faces:

#             cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

#             id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

#             # Check if accuracy is less them 100 ==> "0" is perfect match 
#             if (accuracy < 100):
#                 id = names[id]
#                 accuracy = "  {0}%".format(round(100 - accuracy))
#                 TaskExecution()

#             else:
#                 id = "unknown"
#                 accuracy = "  {0}%".format(round(100 - accuracy))
            
#             cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
#             cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
#         cv2.imshow('camera',img) 

#         k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#         if k == 27:
#             break

#     # Do a bit of cleanup
#     print("Thanks for using this program, have a good day.")
#     cam.release()
#     cv2.destroyAllWindows()

#             # speak("anything else i can do for you sir ")