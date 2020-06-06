import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.support.select import Select
from faker import Faker
from time import sleep
import calendar
import os
import string
import random
import subprocess as sub

def speak(text):
    engine = pyttsx3.init()
 #   voices = engine.getProperty('voices')
 #   engine.setProperty('voice', voices[1].id) #voices[0]/voices[1] can be use, if you want male or female voice
    engine.setProperty('rate',155) #Speed Percent
    engine.setProperty('volume', 20)#Volume
    engine.say(text)
    engine.runAndWait()
    

"""
Setting the Speech Recognizer using Google's Speech Recognition  Library
"""
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

def remove(string): 
    return string.replace(" ", "") 


def password():
    numbers = string.digits
    letters = string.ascii_lowercase
    capletters = string.ascii_uppercase
    alphanumeric = letters + numbers + capletters
    mix = alphanumeric
    intPasswordLength = 12

    Password = ''.join([random.choice(mix) for x in range(intPasswordLength)])
    return Password

def run():

    months = calendar.month_name[1:13]
    dates =  [i for i in range(1,32) ]
    years =  [i for i in range(1990,2000) ]
    outputfile = "Output.json"
    adjetives = ['Expert', 'Gran Master', 'Master', 'Senior', 'Ninja', 'Masine Learning', 'Data Visualisation']
    emaildomains = ['@outlook.com']
    fake = Faker()


    driver = webdriver.Edge()

    driver.get("https://signup.live.com/")

    elem = driver.find_element_by_id("MemberName")

    speak("Tell the username")

    usern = get_audio()
    username = remove(usern)
    print("Email : "+username+"@outlook.com")

    elem.send_keys(username+"@outlook.com")

    driver.find_element_by_id("iSignupAction").click()

    sleep(6)

    elem = driver.find_element_by_id("PasswordInput")

    passwordt = password()
    print("Password : "+passwordt)

    elem.send_keys(passwordt)

    driver.find_element_by_id("iSignupAction").click()

    sleep(3)

    elem = driver.find_element_by_id("FirstName")

    speak("Tell the first name")

    fname = get_audio()
    firstname = remove(fname)

    elem.send_keys(firstname)

    elem = driver.find_element_by_id("LastName")

    speak("tell the last name")

    lname = get_audio()
    lastname = remove(lname)

    elem.send_keys(lastname)

    driver.find_element_by_id("iSignupAction").click()

    sleep(3)

    select = Select(driver.find_element_by_id('Country'))

    countryf=fake.country()

    select.select_by_visible_text(countryf)

    select = Select(driver.find_element_by_id('BirthMonth'))

    month = random.choice(months)

    select.select_by_visible_text(month)

    select = Select(driver.find_element_by_id('BirthDay'))

    date = "{}".format(random.choice(dates))

    select.select_by_visible_text(date)

    select = Select(driver.find_element_by_id('BirthYear'))

    year = "{}".format(random.choice(years))

    select.select_by_visible_text(year)

    driver.find_element_by_id("iSignupAction").click()

    sleep(3)

    
    file_name = username+"@outlook.com" + "-Generate-by-AI_Email.txt"
    with open(file_name, "w") as f:
        f.write("[+]========== This Email is Generated Using Mark42 Email Generator ==========[+]\nDeveloped by Yehan Wasura\n\nEmail : "+ username+"@outlook.com"+"\n\nPassword :" + passwordt)

    sub.Popen(["C:/Windows/notepad.exe", file_name])
    print("\n\n A TXT file has created in the directory, including login credentials")
    speak(" A TXT file has created in the directory, including login credentials")

run()
