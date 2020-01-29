#Importing Libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

#Defining bot profile
bot=ChatBot("CHOTTU")
bot.set_trainer(ChatterBotCorpusTrainer)

#Training the chatbot with corpus
bot.train("chatterbot.corpus.english")

#Getting input and giving response
while(1):
    message=input("You: ")
    if(message!="Bye" or message!="bye"):
        print("{}: {}".format(bot.name,bot.get_response(message)))
    if(message=="Bye" or message=="bye"):
        print("{}: I will really miss you. Bye".format(bot.name))
        break
