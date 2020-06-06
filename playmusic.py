import pygame
import speech_recognition as sr
import os
import random
import glob

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
        command = get_audio();

    return command



def pmusic(file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(1000)
        command = get_audio()

        if command == "stope" or "exit":
            stopmusic()

def stopmusic():
    pygame.mixer.music.stop()


def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

try:

    initMixer()
    file = 
    pmusic(file)
except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
    stopmusic()
    print("\nPlay Stopped by user")
except Exception:
    print("unknown error")

print("Done")