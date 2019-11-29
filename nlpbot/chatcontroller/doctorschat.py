# from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta,date
import logging
import datefinder

from nltk.stem.snowball import SnowballStemmer 
stemmer=SnowballStemmer("english")

from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService
# from .intentclassification import getintent
from .util import getdateandtime,getentities






class DocchatService():
    
    def __init__(self):
        self.DocSer=DocService()
        self.SlotSer=SlotService()
        self.doctors=self.DocSer.getdoctors()

# # **************************
#     def getinput(self):
#         text=input("User:")
#         return text



    def doctorschat(self,intentval):
        # docname=getentities(ques)   department
        # intentval is department
        # print(intentval)
        DocSer=DocService()
        if not intentval:
            doctors=DocSer.getdoctors()
            return "Can you select the doctors from:"+ str(doctors)
        else:
            # print(intentval)
            spec=stemmer.stem(intentval)
            # print(se )
            doctors=DocSer.getdocbydep(spec)
            return doctors
            # print(spec)
 