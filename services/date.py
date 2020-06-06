from Lib.ywPyDT import date
import pyttsx3

def speak(text):
	engine = pyttsx3.init()
#	engine.getProperty('voices', voice[1].id)
#	engine.setProperty('voices', voice[1].id)
	engine.setProperty('rate',155) #Speed Percent
	engine.setProperty('volume', 0.4)#Volume
	engine.say(text)
	engine.runAndWait()


today= date.today()

date = today.strftime("%d  %B  %Y")
speak("Today is : " + date)
print("Today is : " + date)

