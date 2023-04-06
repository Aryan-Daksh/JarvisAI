import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print("Jarvis Starting....")
print("Voice Id =",voices[1].id)
engine.setProperty('voice' ,voices[0].id)
count=1
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Sir Daksh!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon,Sir Daksh!")
    else:
        speak("Good Evening,Sir Daksh!")

    speak("I am Friday. Please Tell me How May I Help You?")
def takeCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        speak('listening')
        print("Listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio , language="en-in")
        print("User said: ",{query})


    except Exception as engine:
          global count
          count = count + 1
          if count!=5:
            speak("Say That Again Please....")


          print(count)
          if count == 5:
             speak('No Speech detected..Terminating Protocol')
             exit()

          return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)


if __name__=="__main__":
    wishMe()
    while True:
       query=takeCommand().lower()

       if 'time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir..The Time is.. {strTime}")


       elif 'exit' in query:
           speak('Terminating Protocol')

           hours=int(datetime.datetime.now().hour)
           if hours>=5 and hours<18:
               speak("Have A Good Day Sir!!")

           else:
               speak("Have A Good Night Sir!!")

           exit()

       elif 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query=query.replace("Wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           speak(results)


       elif 'youtube' in query:
           webbrowser.open("youtube.com")

       elif 'browser' in query:
           speak('Opening Browser at Your Request')
           webbrowser.open('https://google.com')

       elif 'code' in query:
           codePath= "C:\\Users\\aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

       elif 'email' in query:
           try:
               speak("What Should I say?")
               content=takeCommand()
               to= "yourEmailID@gmail.com"
               sendEmail(to,content)
               speak("Email Has Been Sent")
           except Exception as e:
               print(e)
               speak("Email cant be send")


