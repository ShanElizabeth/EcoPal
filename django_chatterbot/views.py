from django.shortcuts import render,render_to_response
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer
import logging 
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

chatbot=ChatBot('EcoPal')

# Train based on the english corpus
#chatbot.train("chatterbot.corpus.english")
#conv= open('chat.txt','r').readlines()

#trainer=ListTrainer(chatbot)
#trainer.train(conv)

# Create your views here.
def displaypage(request):
    return render(request,'chat.html')  


def get_response(request):
    response={'status':None}
    print("in view")

    if request.method=='POST': #if its a post method go into this if
        data=json.loads(request.body)#get value for user inout
        message=data['message']

        chat_response=chatbot.get_response(message).text #get repoonse from chatbt
        response['message']={'text':chat_response,'user':False,'chat_bot':True} #update dictionary
        response['status']='ok'
    else:
        response['error']='no post data found'

    return HttpResponse(
        json.dumps(response), #print as stringgs
        content_type="application/json"
        )
"""
class ChatterBotApiView(View):

   # Provide an API endpoint to interact with ChatterBot.
    
    print("in class")
    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        
    #    print
 #       Return a response to the statement in the posted data.
#
  #      * The JSON data should contain a 'text' attribute.
        
        print("in post view")
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        
   #     Return data corresponding to the current conversation.
        
        return JsonResponse({
            'name': self.chatterbot.name
        })
        
"""