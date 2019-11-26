# from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
import logging

from nlpbot.chatcontroller.appointmentchat import AppchatService
from nlpbot.chatcontroller.doctorschat import DocchatService
from nlpbot.chatcontroller.slotschat import SlotchatService
from .intentclassification import getintent
from rest_framework.views import APIView


logger=logging.getLogger(__name__)

class NlpView(APIView):

    def __init(self):
        self.Appchat=AppchatService()
        self.Docchat=DocchatService()
        self.Slotchat=SlotchatService()

    def index(self,request):
        reply={}
        reply['message']="Hi!! Book an Appointment"
        return HttpResponse("Hi, Book an Appointment")

    # to get inputs from the user
    def getinput(self):
        text=input("User:")
        return text

    # to classify the intent for the text sentence
    def run(self):
        self.Appchat=AppchatService()
        self.Docchat=DocchatService()
        self.Slotchat=SlotchatService()
        while True:
        # print("User:")
            ques=self.getinput()
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
                    response=self.Docchat.doctorschat(intent_val)
                else:
                    response=self.Docchat.doctorschat(intent_val)
            elif intent=="appointment":
                response=self.Appchat.appointmentchat(ques)
            elif intent=="slots":
                response=self.Slotchat.slotschat(ques)
            elif intent=="greet":
                response="Hi,What are you looking for?"
            elif intent=="affirm":
                response="Okay"

            print("Bot:"+str(response))

