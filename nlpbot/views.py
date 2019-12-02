# from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging

from nlpbot.chatcontroller.appointmentchat import AppchatService
from nlpbot.chatcontroller.doctorschat import DocchatService
from nlpbot.chatcontroller.slotschat import SlotchatService

from rasafiles.intentclassification import getintent
from rest_framework.views import APIView
from rest_framework.response import Response
from nlpbot.chatcontroller.util import getentities

logger=logging.getLogger(__name__)

class NlpView(APIView):

    def __init(self):
        self.Appchat=AppchatService()
        self.Docchat=DocchatService()
        self.Slotchat=SlotchatService()

    def get(self,request):
        # reply={}
        # reply['message']="Hi!! Book an Appointment"
        return render(request,'new.html')

    # to get inputs from the user
    def getinput(self):
        text=input("User:")
        return text

    def slot(self,ques):
        response=self.Slotchat.slotschat(ques)
        return response
    
    def doctor(self,ques):
        intent_val=""
        intent_struc=ques
        if intent_struc['entities']:
            intent_val=intent_struc['entities'][0]['value']
            response=self.Docchat.doctorschat(intent_val)
        else:
            response=self.Docchat.doctorschat(intent_val)
        return response

    def doctorsug(self):
        intent_val=""
        response=self.Docchat.doctorschat(intent_val)
        return response
    
    def appointment(self,ques):
        response=self.Appchat.appointmentchat(ques)
        return response
    
    def greet(self,ques):
        return "Hi,What are you looking for?"
    
    def affirm(self,ques):
        return "Okay" 

    # to classify the intent for the text sentence
    def run(self):
        self.Appchat=AppchatService()
        self.Docchat=DocchatService()
        self.Slotchat=SlotchatService()
        while True:
            switcher={
            "slots": self.slot,
            "doctors": self.doctor,
            "appointment":self.appointment,
            "greet":self.greet,
            "affirm":self.affirm,
            "doctorsug":self.doctorsug
            }
            ques=self.getinput()
            intent_struc=getintent(ques)
            intent=intent_struc['intent']['name'] 
            
            randname=getentities(ques)
            print(intent)
            if intent=="goodbye":
                print("Bye")
                break
            elif len(ques.split())<=2 and randname:
                func = switcher.get("doctorsug", "nothing")
                resp=func()
            else:
                if intent=="doctors":
                    ques=intent_struc
                func = switcher.get(intent, "nothing")
                resp=func(ques)
            print("Bot:"+str(resp))


