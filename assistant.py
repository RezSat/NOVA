import os
import pyttsx3
import platform
import speech_recognition as sr
from pocketsphinx import LiveSpeech
import Lib.ywBrowser as yb
import re
import pyautogui as auto
import subprocess as sub
import datetime
import random
import time
import sys




"""
Creating the Speech with pyttsx3 library
"""
def speak(text):
    engine = pyttsx3.init()
 #   voices = engine.getProperty('voices')
 #   engine.setProperty('voice', voices[1].id) #voices[0]/voices[1] can be use, if you want male or female voice
    engine.setProperty('rate',155) #Speed Percent
    engine.setProperty('volume', 120)#Volume
    engine.say(text)
    engine.runAndWait()

    
#----------------------------------------------#

#Setting the Speech Recognizer using Google's Speech Recognition  Library[Online]

def get_audio():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said: "+ command + '\n')

    except sr.UnknownValueError:
        print("Error : i don't understand")
        speak("i don't understand")
        command = get_audio()

    return command

#---------------------------------------------#

#Setting up the recognizer with pocketsphinx[Offline]

#---------------------------------------------#
'''
hmm   ='en-us'
lm    ='lanmodel/0552.lm'
dicts ='lanmodel/0552.dict'
speak("Hello commander, I am Norva GTXS3. your AI personal Assistant ")

recognizer = LiveSpeech(verbose=False , sampling_rate=16000 ,buffer_size=2048, no_search=False, full_utt=False, 
    hmm=hmm ,lm=lm , dic=dicts)
'''
#---------------------------------------------#
def note(command):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(command)

    sub.Popen(["C:/Windows/notepad.exe", file_name])

#---------------------------------------------#

def assistant(command):


    GREE_STRS = ["end","nova over","over","off","go offline"]
    for phase in GREE_STRS:
        if phase in command:
            print("NOVA : "+"Good Bye , I am your personal assistant NOVA\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            quit()


    GRE_STRS = ['hello','oh','how are you',"what's up"]
    for phase in GRE_STRS:
        if phase in command:
            print("NOVA : "+"Fine,How are you sir, I am Nova , your peronal assistant, what should I do for you.")
            speak("Fine , how are you commander , what should i do for you")

    NOTE_STRS = ['remember this','make a note','note this']
    for phase in NOTE_STRS:
        if phase in command:
            speak("what would you like me to write down")
            note_text = get_audio()
            note(note_text)
            speak("I have made a note of that commander")

    ReG_STR = ['open reddit','go to reddit']
    for phase in ReG_STR:
        if phase in command:
            speak("Opening Reddit")
            yb.open("https://www.reddit.com/")


    google_STR = ['open google','go to google']
    for phase in google_STR:
        if phase in command:
            speak("Opening Google")
            yb.open("https://www.google.com/")

    Yt_STR = ['open youtube','go to youtube']
    for phase in Yt_STR:
        if phase in command:
            speak("Opening Youtube")
            yb.open("https://www.youtube.com/")

    gitH_STR = ['open github','go to github']
    for phase in gitH_STR:
        if phase in command:
            speak("Opening git hub")
            yb.open("https://www.github.io/")

    faceb_STR = ['open facebook','go to facebook']
    for phase in faceb_STR:
        if phase in command:
            speak("Opening facebook")
            yb.open("https://www.facebook.com/")

    inst_STR = ['open instagram','go to instagram']
    for phase in inst_STR:
        if phase in command:
            speak("Opening instagram")
            yb.open("https://www.instagram.com/")

 # Add more sites if you need

    date_STR = ["today's date","what's the date today"]
    for phase in date_STR:
        if phase in command:
            today= datetime.date.today()
            date = today.strftime("%d  %B  %Y")
            print("Today is : " + date)
            speak("Today is : " + date)

    time_STR = ['time now',"time please","what's the time now"]
    for phase in time_STR:
        if phase in command:
            import services.time_now

    game_STR = ['play game',"run game","play a game","run a game"]
    for phase in game_STR:
        if phase in command:
            speak("playing snake game")
            import gamePlay

    music_STR = ['play a music','play music','play a song','play song']
    for phase in music_STR:
        if phase in command:
            speak("playing a music")
            import playmusic

    wiki_Serch = ['search wikipedia','wikipedia search','can you search wikipedia']
    for phase in wiki_Serch:
        if phase in command:
            import services.wikisearch

    AI_EMAIL = ['make me an email','generate an email','create an outlook email','nova create an email account',"make a mail"]
    for phase in AI_EMAIL:
        if phase in command:
            import AI_Email

    MIN_WIN = ['minimize','minimize this window','hide this window','hide the window','minimise','minimise this window']
    for phase in MIN_WIN:
        if phase in command:
            auto.hotkey('winleft','down')
            speak("window minimized")

    MAX_WIN = ['maximize','maximize this window','enlarge this window','maximise','maximise this window']
    for phase in MAX_WIN:
        if phase in command:
            auto.hotkey('winleft','up')
            speak("window maximized")

    EXIT_WIN = ['close this window','exit from here','exit the window','close the window','exit','close','exit from here']
    for phase in EXIT_WIN:
        if phase in command:
            auto.hotkey('alt','f4')
            speak('window closed')

    SCRN_SHOT = ['take a screen shot','take a shot here','screen shot here','screenshot here']
    for phase in SCRN_SHOT:
        if phase in command:
            auto.screenshot()
            speak('screen shot it taken')

    COPY_TXT = ['copy this text','copy it','copy here','copy this']
    for phase in COPY_TXT:
        if phase in command:
            auto.hotkey('ctrl','c')
            speak("copied")

    PASTE_TXT = ['paste here','paste it','paste now']
    for phase in PASTE_TXT:
        if phase in command:
            auto.keyDown('ctrl')
            auto.press('v')
            auto.keyUp('ctrl')
            speak('pasted')

    WEB_STR = ['open web browser','run web browser']
    for phase in WEB_STR:
        if phase in command:
            yb.open()

    CMD_STR = ['open cmd','run cmd','open command prompt','run command prompt','open terminal']
    for phase in CMD_STR:
        if phase in command:
            sub.Popen(['C:/Windows/System32/cmd.exe'])

    WEB_SEAR = ['web search','search on web','search google','search for this']
    for phase in WEB_SEAR:
        if phase in command:
            import websearch

    WHOIS = ["what's your name",'who are you','what is you','introduce yourself','introduce you for new authorized people']
    for phase in WHOIS:
        if phase in command:
            print("NOVA : "+"I am norva X4.2,I am a Computational Intelligent Digital Assistant ,Powered by Python.I am one of the Excellent Project of Yehan Wasura. So I am the newer version Mark and Known as Mark 42 as well")
            speak("I am norva X4.2,I am a Computational Intelligent Digital Assistant ,Powered by Python.I am one of the Excellent Project of Yehan Wasura. Also I am the newer version Mark and Known as Mark 42 as well")

    WO_BUI = ['who built you','who is your creator',"what's the name of your creator"]
    for phase in WO_BUI:
        if phase in command:
            print("NOVA : "+"My creator is Yehan Wasura. Who is a programmer a Ethical Hacker and a Computer Science Student. I am a Project of Him")
            speak("My creator is Yehan Wasura. Who is a programmer a Ethical Hacker and a Computer Science Student. I am a Project of Him")

    CAL_STR = ['add','subtract','divide','multiply','calculate','python cal']
    for phase in CAL_STR:
        if phase in command:
            import test.maths


    

#loop to continue executing multiple commands
speak("Hello commander, I am Norva GTXS3. your AI personal Assistant ")

while True:
    assistant(get_audio())

'''
   {Use this Loop when you use PocketSphinx}
while True:
    print("Listening...")
    for phrase in recognizer:
        command = str(phrase)
        print("You Said : " + command+'\n')
        if assistant(command) == -1:
            break
''' 