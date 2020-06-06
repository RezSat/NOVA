from datetime import datetime
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
 #   voices = engine.getProperty('voices')
 #   engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',155) #Speed Percent
    engine.setProperty('volume', 20)#Volume
    engine.say(text)
    engine.runAndWait()


def time():
	now = datetime.now()

	hour = str(now.hour)

	mi = str(now.minute)

	ss = str(now.second)

	twl = "12"

	if hour == "12":
		print("12'O Clock")
		speak("12 o clock")

	elif hour == "13":
		print("1"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("1"+ mi+"pm")

	elif hour == "14":
		print("2"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("2"+ mi+"pm")

	elif hour == "15":
		print("3"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("3"+ mi+"pm")

	elif hour == "16":
		print("4"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("4"+ mi+"pm")

	elif hour == "17":
		print("5"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("5"+ mi+"pm")

	elif hour == "18":
		print("6"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("6"+ mi+"pm")

	elif hour == "19":
		print("7"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("7"+ mi+"pm")

	elif hour == "20":
		print("8"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("8"+ mi+"pm")

	elif hour == "21":
		print("9"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("9"+ mi+"pm")

	elif hour == "22":
		print("10"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("10"+ mi+"pm")

	elif hour == "23":
		print("11"+"h"+" : "+mi+"m"+" : "+ss+"s"+" P.M.")
		speak("11"+ mi+"pm")

	elif hour == "24":
		print("12'O Clock")
		speak("12 O clock")	

	elif hour > twl:
		print(hour+"h"+" : "+mi+"m"+" : "+ss+"s"+" A.M.")
		speak(hour+ mi+"am")

time()


