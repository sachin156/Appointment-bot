# from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import logging

from nlpbot.chatcontroller.appointmentchat import AppchatService
from nlpbot.chatcontroller.doctorschat import DocchatService
from nlpbot.chatcontroller.slotschat import SlotchatService
from .intentclassification import getintent

logger=logging.getLogger(__name__)


Appchat=AppchatService()
Docchat=DocchatService()
Slotchat=SlotchatService()

def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")

def getinput():
    text=input("User:")
    return text

# # ***************************   
def run():
    while True:
    # print("User:")
        ques=getinput()
        intent_struc=getintent(ques)
        intent=intent_struc['intent']['name']
        # print(intent)
        if intent=="goodbye":
            print("Bye")
            break

        elif intent=="doctors":
            intent_val=""
            if intent_struc['entities']:
                intent_val=intent_struc['entities'][0]['value']
                response=Docchat.doctorschat(intent_val)
            else:
                response=Docchat.doctorschat(intent_val)
        elif intent=="appointment":
            response=Appchat.appointmentchat(ques)
        elif intent=="slots":
            response=Slotchat.slotschat(ques)
        elif intent=="greet":
            response="Hi,What are you looking for?"
        elif intent=="affirm":
            response="Okay"

        print("Bot:"+str(response))

