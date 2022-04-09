import os
import speech_recognition as sr

def takeCommand():

    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('listening...')
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print("Recognizing...")
                print(f"User said: {command}\n")    

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return command

while True:
    wake_up = takeCommand()

    if 'wake up' in wake_up:
        os.startfile('C:\\Users\\SOUMYAJIT\\Python Projects\\python\\Jarvis\\Jarvis.py')

    else:
        print('Nothing...')    
