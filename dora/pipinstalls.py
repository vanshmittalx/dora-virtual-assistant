#installing required packages from terminal to run the voice assistant
import subprocess
def installer():
    commands = ["pip install setuptools","pip install speechrecognition pyaudio","pip install pyttsx3","pip install requests", "pip install openai","pip install gtts","pip install pygame"]
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
installer()