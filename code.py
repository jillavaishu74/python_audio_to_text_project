import speech_recognition as sr
r=sr.Recognizer()
with sr.AudioFile(r"..........file path.........mp3")as source:
  audio=r.record(source,duration=None)
try:
  text=r.recognize_google(audio)
  print("working on audio....")
  print(text)
except:
  print("sorry try again")
  
  
