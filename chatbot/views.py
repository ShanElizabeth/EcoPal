from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .models import saveAnswer
from django.contrib.auth.models import User
#chatbot modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging 
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot=ChatBot('EcoPal',
	logic_adapters=[ {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.60
            }

	]
	)

conv= open('chatbot/chat.txt','r').readlines()

trainer=ListTrainer(bot)
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")
trainer.train(conv)

@csrf_exempt
def getResponse(request):
	text = request.POST['Question']
	ecolpalresponse=select_response(text,conv)
	print (ecolpalresponse)
	return HttpResponse(ecolpalresponse)

def select_response(statement, statement_list, storage=None):
	statement=statement+"\n"
	#statementcap=statement.capitalize()
	for i in range(0,len(conv)-1):
		if conv[i]==statement :#or statementcap:
			ecolpalresponse=conv[i+1]
			return ecolpalresponse
		else:
			return bot.get_response(statement)
		#else:
		#	return (bot.get_response(statement))
#def chatbotresponse(text):
 # ecolpalresponse=bot.get_response(text)
  #return (ecolpalresponse )

def display(request):
  return render(request,'response.html')

@csrf_exempt
def saveanswer(request):
	answers=request.POST['Answer']
	obj=saveAnswer()
	obj.answer=answers
	Uname=request.user
	obj.user=User.objects.get(username=Uname)
	obj.save()
	return HttpResponse("Working")
	#lse:

	#	return HttpResponse({"not okay"})


#def getAnswer(request):
#	text=request.POST['Question']
#	conv=('chatbot/chat.txt','r').readlines()
#	conv=conv.splt("?")
#	print (conv)