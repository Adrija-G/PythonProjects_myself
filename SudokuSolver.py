import speech_recognition as sr 
import pyttsx3  
listener= sr.Recognizer()   #Interprets ("recognises") user-input voice messages 
engine= pyttsx3.init()      #Initialising engine that will speak to us
engine.say('Hello! I am Siri, your virtual AI assistant!')
engine.runAndWait()
try:
    with sr.Microphone as source: # Microphone is the "source" of sound
        
        print('Listening...')
        voice= listener.listen(source)  #Making listener (AI) listen to the source (user)
        command= listener.recognize_google(voice)   #Voice input sent to Google API which converts it to textual command
        command= command.lower()
        if 'Siri' in command:        
            print(command)                   #Making sure the above command is working
except:
    pass