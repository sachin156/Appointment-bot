from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import string
import datefinder
from itertools import groupby
import operator

import nltk
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService
from .intentclassification import getintent

logger=logging.getLogger(__name__)

# **************
st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
# *************
def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")


DocSer=DocService()
doctors=DocSer.getdoctors()

def doctorschat(text):
    # docname=getentities(ques)   department
    DocSer=DocService()
    doctors=DocSer.getdoctors()
    return doctors

def slotschat(text):
    docname=getentities(text)
    DocSer=DocService()
    doctors=DocSer.getdoctors()     
    if docname:
        SlotSer=SlotService()
        msg=SlotSer.docslots(docname)
        return (msg)
    else:
        return ("Select any doctor from the suggested:"+str(doctors))

def appointmentchat(text):
    # docname=getentities(ques)
    matches=list(datefinder.find_dates(text))
    # print(matches)
    if not matches:
        # return HttpResponse("Enter date and time to make the appointment")
        print("Bot:Enter date and time to make the appointment")
        text=input("User:")
        appointmentchat(text)
    else:
        start_time=matches[0]
        userday=str(start_time).split(" ")[0]
        usertime=start_time.strftime('%H:%M')

    if datetime.now()>start_time:
        logger.exception("Exception:Enter Valid Date and Time")
        print("Appointment not created,select from other timings")
    if docname:
        start_time=matches[0]
        userday=str(start_time).split(" ")[0]
        usertime=start_time.strftime('%H:%M')
        appser=AppService()
        # patient name
        # print(docname)
        msg=appser.bookappointment(docname,usertime,"Y",userday,"srinu",text)
        return (msg)
    else:
        return ("Select any doctor from the suggested:"+str(DocSer.getdoctors()))
    

def getentities(text):
    # intent=getintent(text)

    tokenized_text = (word_tokenize(text.title()))
    # ner tagging 
    classified_text = st.tag(tokenized_text)

       # # objs for service classes....
    

    doctor=""
    docname=""
    for tag, chunk in groupby(classified_text, lambda x:x[1]):
        if tag== "PERSON":
            doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
            docname=doctor[1].lower()
            return docname

while True:
    # print("User:")
    ques=input("User:")
    intent=getintent(ques)
    if intent=="goodbye":
        print("Bye")
        break
    elif intent=="doctors":
        response=doctorschat(ques)
    elif intent=="appointment":
        response=appointmentchat(ques)
    elif intent=="slots":
        response=slotschat(ques)
    print("Bot:"+str(response))
