import speech_recognition
import random
from datetime import date
import pyttsx3

ai_brain = ""
ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()

while True: 
	with speech_recognition.Microphone() as mic:
		print("AI: I'm listening")
		audio = ai_ear.listen(mic)
	print("AI:....")
	try:
		you = ai_ear.recognize_google(audio)
	except:
		you == ""

	print("You: " + you)

	if you == "":
		ai_brain = "I can't hear you, try again!"
	elif "how are you" in you:
		response = ["I'm fine thank you and you?", "Awesome, what about you?", "Totally great! You?"]
		ai_brain = random.choice(response)
	elif "today" and "date" in you:
		today = date.today()
		ai_brain = "Today is " + today.strftime("%B %d, %Y")
	elif "bye" in you:
		ai_brain = "Bye friend! See you later!"
		print("AI: " + ai_brain)
		ai_mouth. say(ai_brain)
		ai_mouth.runAndWait()
		break
	else:
		ai_brain = "Hello there!"
	
	print("AI: " + ai_brain)
	ai_mouth. say(ai_brain)
	ai_mouth.runAndWait()
