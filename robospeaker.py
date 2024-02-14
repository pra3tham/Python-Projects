import os

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. Created by Pratham.")
    while True:
        x=input("Enter what you want me speak.")Pratham
        if x == "bye":
            break
        command= f"PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak{x}"
        os.system(command) 