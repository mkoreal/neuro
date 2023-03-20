import pyttsx3

# settings
tts = pyttsx3.init()

rate = tts.getProperty('rate')
print(rate)
tts.setProperty('rate', 150)

volume = tts.getProperty('volume')
print(volume)

voices = tts.getProperty('voices')
print(*voices)

tts.say('Привет!')
tts.runAndWait()