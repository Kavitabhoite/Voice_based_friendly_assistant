import imaplib
import speech_recognition as sr
import easyimap as e
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib


r = sr.Recognizer()

engine = pyttsx3.init()                                               #Defining an engine for text to speech
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.setProperty('rate' , 150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noice(source)
        str = "Speak Now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)                            #the voice is recognized using the google voice recognition API
            return text
        except:
            str = "Sorry could not recognize what you said."
            speak(str)


unm = "**************@gmail.com"                                    #login credentials of our emial id
pwd = "****************"

def sendmail():                                                          #function to send email
    rec = "****************8@gmail.com"

    str = "Please speak the body of the message"
    speak(str)
    msg = listen()

    str = "You have spoken the message."
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)                    #local host server
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been sent."
    speak(str)

def readmail():
    server = e.connect("imap.gmail.com",unm,pwd)
    server.listids()

    str = "Please say the serial number of the email you wanna read starting from the latest."
    speak(str)

    a = listen()
    if(a == "tu"):
        a = "2"
        print(a)

    b = int(a) - 1                          #take byte values as input

    email = server.mail(server.listids()[b])

    str = "The email is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the email is: "
    speak(str)
    speak(email.title)
    str = "The body of the email is: "
    speak(str)
    speak(email.body)


def youtube():
    str = "What song you wanna listen."
    speak(str)
    song = listen()

    str = "playing "
    speak(str)
    speak(song)
    pywhatkit.playonyt(song)
    engine.runAndWait()


def time():
    str = "The current time is : "
    speak(str)
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(time)

def search():
    str = "Tell the name of the person you wanna know about."
    speak(str)
    person = listen()

    str = "Result is : "
    speak(str)
    about = wikipedia.summary(person, 2)
    speak(about)

    
def jokes():
    speak(pyjokes.get_joke())


str = "Welcome! This is your voice based friendly assistant."
speak(str)

while(1):
    str = "What do you want to do?"
    speak(str)

    str = "Speak SEND to send email     Speak READ to read email    Speak PLAY to play songs    Speak TIME to know the current time   Speak SEARCH to search on wikipedia   Speah JOKE for entertainment  Speak EXIT to exit     "
    speak(str)

    ch = listen()
    if(ch == 'send'):
        str = "You have choosen to send an email."
        speak(str)
        sendmail()
        str = "Now........"
        speak(str)

    elif(ch == 'read'):
        str = "You have choosen to read an email."
        speak(str)
        readmail()
        str = "This is the mail you want to read."
        speak(str)
        str = "Now........"
        speak(str)

    elif(ch == 'exit'):
        str = "You have choosen to exit, Good Bye!!"
        speak(str)
        exit(1)

    elif (ch == 'play'):
        youtube()
        break;

    elif (ch == 'time'):
        time()
        str = "Now........"
        speak(str)

    elif (ch == 'search'):
        search()
        str = "That's all about you asked."
        speak(str)
        str = "Now........"
        speak(str)

    elif (ch == 'joke'):
        jokes()
        str="Hope you enjoyed."
        speak(str)
        str="Now........"
        speak(str)

    else:
        str = "Invalid choice. You said : "
        speak(str)
        speak(ch)
