import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''
    this func for speak by computer
    '''
    engine.say(audio)
    engine.runAndWait()



def wishme():
    '''
    this func is wish you about time
    '''
    Hour=int(datetime.datetime.now().hour)
    if Hour>=0 and Hour<=12:
        speak("good morning")
    elif Hour>12 and Hour<=18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("hii helper! how are you...")

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
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    takeCommand()