import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Neha. How have you been?")
    
    time()    
    date()
    hour = datetime.datetime.now().hour
    if hour >=5 and hour <12:
        speak("Good Morning Ma'am!")
    elif hour >=12 and hour <17:
        speak("Good Afternoon Ma'am!")
    elif hour >=17 and hour <24:
        speak("Good Evening Ma'am!")
    else:
        speak("It's too late, Good night and sleep well ma'am.")
    speak("Stark is at your service, Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(query)    

    except Exception as e:
        print(e)
        speak("Sorry, I didn't hear you. Please repeat again.")  

        return "None"
    return query  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nehagpt692@gmail.com', '*********')
    server.sendmail('nehagpt692@gmail.com', to, content)
    server.close()

def screenshot():
    image = pyautogui.screenshot()
    image.save("C:\\Users\\NEHA GUPTA\\Visual Code Files\\ss.png")

def CPU():
    cpu_usage = str(psutil.cpu_percent())
    speak('CPU is at' +cpu_usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'nehagup665@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email!")
        elif 'search in chrome' in query:
            speak("What shall I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system('logout -l')
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            os.system('restart /r /t 1')
        elif 'play songs' in query:
            songs_directory = "D:\\Songs\\Attention - Charlie Puth.mp3"
            songs = os.listdir(songs_directory)
            os.startfile(os.path.join(songs_directory, songs[0]))
           # time.sleep(2000)
        elif 'remember that' in query:
            speak("What shall I remember?")
            data = takeCommand()
            speak("You told me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("You told me to remember that" +remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot taken successfully!")
        elif 'CPU' in query:
            CPU()
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            speak("Bye Neha. See you soon!")
            quit()
