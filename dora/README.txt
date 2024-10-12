Before running the virtual assistant, make sure you install the necessary packages and libraries on your computer
Step 1:
Run the 'pipinstalls.py' file to install the packages
- speechrecognition
- pyaudio
- pyttsx3
- requests
- openai
- gtts
- pygame

Step 2:
When finished run the 'main.py' file to run Dora
Step 3:
Dora will respond to commands when activated. To activate Dora say "Dora" and it will respond upon activation. You can further use the assistant to do whatever you feel like
Step 4:
Dora will respond to other commands after being activated for each command.

NOTE:
- The voice assistant will work and give AI responses through openai after generating an API key through OpenAI. To generate a user key for your system visit https://openai.com/index/openai-api/ and signup and get your API key and paste your API key in main.py file in line 42 where api_key = <Your Key Here>
- Similarly you will have to generate NEWSAPI key (line 16) to listen to news through the assistant
- You can save links to your favorite music in 'musicLibrary.py' file and Dora will play them when asked