import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    "voice", voices[1].id
)  # changing index, changes voices. 1 for female

volume = engine.getProperty(
    "volume"
)  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty("volume", 1)

rate = engine.getProperty("rate")  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty("rate", 150)  # setting up new voice rate


engine.say("My name is Arash")

engine.runAndWait()
