import requests
from gtts import gTTS
import os
import time

url = "https://official-joke-api.appspot.com/jokes/random"

data = requests.get(url).json()

setup =  data['setup'] 
punchline = data['punchline']
print(setup + '\n' + punchline)
setup_voice = gTTS(text=setup, lang='en', slow=False)
punchline_voice = gTTS(text=punchline, lang='en', slow=False)

setup_voice.save("setup.mp3")
punchline_voice.save("punch.mp3")

os.system("C:/mpg123-1.26.4-x86-64/mpg123-1.26.4-x86-64/mpg123.exe setup.mp3")
time.sleep(5)
os.system("C:/mpg123-1.26.4-x86-64/mpg123-1.26.4-x86-64/mpg123.exe punch.mp3")
