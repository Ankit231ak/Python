import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  

while True:
    text = input("Enter the text (q to quit): ")
    if text.lower() == 'q':
        break
    elif text.strip() == "":
        print("❌ Please enter some text.")
    else:
        speak(text)
        print("Speaking:", text)
