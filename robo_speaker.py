import os
import pyttsx3 as tts


if __name__=='__main__':
    
    command = tts.init()
    
    rate=command.getProperty('rate')
    
    command.setProperty('rate',150)
    
    command.say("hey i am a robo speaker 1.1 created by 'Deep'. I am his Personal Speaker.")
    command.say("What do you want me to say.")
    
    command.runAndWait()
    
    while True:
        x=input("enter the text : ")
        
        if (x=="b"):
            
            command.say("Shutting Down.")
            
            command.runAndWait()
            break
        
        command.say(f"{x}")
    
    
        command.runAndWait()
