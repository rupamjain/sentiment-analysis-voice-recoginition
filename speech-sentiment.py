from textblob import TextBlob
import speech_recognition as sr


#part-1 Get the text from speech
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")


#part-2 Predict sentiment from text 
if 'text' in locals():
  text=TextBlob(text)

  text=text.sentiment.polarity

  print(text) #This prints polarity

  if text>0:
            result="positive"
  elif text<0:
            result="negative"
  else:
            result="nuetral" 


  print(result)

