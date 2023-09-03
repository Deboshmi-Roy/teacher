from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk() 
root.geometry("500x500")
root.configure(background="Light Pink")

label=Label(root,text="Happy Teacher's Day  Saptarshi Sir",bg="Light Pink",fg="Snow2",
font=("Bahnschrift Light",35,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label=Label(root,text="I was lost but you guided me to the right path",bg="Light Pink",fg="Turquoise1",
font=("Italic",25,"bold"))
label.place(relx=0.5,rely=0.4,anchor=CENTER)

text_to_speech=pyttsx3.init() 
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("")
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source) 
        voice_data='' 
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in') 
        except sr.UnknownValueError: 
                print('Please repeat i did not get that')
                speak("Please repeat I did not get that")
        respond(voice_data)
        
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data) 
    if "name" in voice_data:
        speak("My name is Deboshmi")
        print("My name is Deboshmi")
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "hello" in voice_data:
        speak("Happy Teacher's Day Sir")
        webbrowser.get().open("https://www.highclap.com/images/teachers-day-poems/teacher-day-poem-2.jpg")
        
 
btn=Button(root, text="Start",bg="red3",fg="white", padx=10,pady=1,
font=("Ariel",11,"bold"),relief=FLAT,  command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)


root.mainloop()
