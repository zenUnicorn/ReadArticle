#Description: This takes text from an online article and converts it to speech(program that read articles online while you rest.)

#A text to speech program using python.
#Perequistes: Python 3, Libraries( NLTK, gTTS )

#Immport the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the Article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv4lu3xwx')

#Download the article.
article.download()
#parse the article
article.parse()

nltk.download('punkt') #Download the punkt package
article.nlp() #Apply NLP

#Get the article text and store it into a variable called 'mytext'
mytext = article.text

Print(mytext)

language = 'en' #English

#Convert the Text to Speech
myobj = gTTS(text=mytext, lang=language, slow=False)

#Save the converted article as a file
myobj.save('read_article.mp3')

#Play the converted file
os.system('start read_article.mp3')
