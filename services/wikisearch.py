import pyttsx3 
import speech_recognition as sr 
import wolframalpha 
import wikipedia 


def speak(text):
    engine = pyttsx3.init()
 #   voices = engine.getProperty('voices')
 #   engine.setProperty('voice', voices[1].id)
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



command = get_audio()
query = command
try: 
	app_id = "A76PUG-AQXWU7XKQW"
	client = wolframalpha.Client(app_id) 
	res = client.query(query) 
	answer = next(res.results).text 
	print(answer) 
	speak("Your answer is " + answer)

except: 
    
	query = query.split(' ') 
	query = " ".join(query[0:]) 
	speak("I am searching for " + query) 
	print(wikipedia.summary(query, sentences = 3)) 
	speak(wikipedia.summary(query, sentences = 3)) 
	
query = query.split(' ') 
query = " ".join(query[0:]) 
speak("I am searching for " + query) 
print(wikipedia.summary(query, sentences = 3)) 
speak(wikipedia.summary(query, sentences = 3)) 
 