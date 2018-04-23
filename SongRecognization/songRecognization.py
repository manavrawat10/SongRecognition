# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:19:24 2018

@author: Manvenddra
"""

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
# pip install SpeechRecognition
#pip install pyaudio
#pip install bs4


import speech_recognition as sr
from time import ctime
import time
import os
import bs4 as bs
import requests
#from gtts import gTTS
import webbrowser
import platform
syss=platform.system()
if syss=='Windows':
    import win32com.client as wincl
    speakss = wincl.Dispatch("SAPI.SpVoice")

def speak(audioString):
    print(audioString)
    speakss.Speak(audioString)
 
    
#this part is for listening.....
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes am listening.")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def maddy(data):
    speak("Hold on for a second, I am still processing. I think I have heard this one.....")
    url="https://www.youtube.com/results?search_query="+str(data.replace(" ","+"))+"+youtube"
    print(url)
    res=requests.get(url)
    doc=str(res.text)
    soup = bs.BeautifulSoup(doc,"lxml")
    score=[]

    for div_tags in soup.find_all('div', attrs={"class": "yt-lockup-content"}):
        score.append(div_tags.text)
    speak(score[0].split('-')[0])
    link=[]
    for a_tags in soup.find_all('a', attrs={"class":"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "}):
        link.append(a_tags['href'])
    ln="www.youtube.com"+str(link[0])
    speak("Do you want me to play that song for you on youtube ?")
    play=recordAudio()
    if "yes" in play:
        webbrowser.open(ln)
    speak("Thanks for using me... Have a nice day")

# initialization

time.sleep(2)
speak("Hi. May I know your name please:")
name=recordAudio()
while len(name)==0:
	speak("Hi. May I know your name please:")
	name=recordAudio()
speak("Hi "+name+", thats very good name. Can you please sing the song for me once. ")
data = recordAudio()
while len(data)==0:
	speak("Sorry I was busy some where else. Can you please sing again.")
	data=recordAudio()
maddy(data)
