import webbrowser as wb
import pyttsx3
import speech_recognition as sr

"""
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

"""


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
      print('Your command is not clear enough')
      command = get_audio();

    return command

def main():

  speak('Yes, commander what you whant to search out')
  query = get_audio()
  url = "htthttps://www.google.com/search?q="+query
  wb.open(url)

if __name__ == '__main__':
	main()
