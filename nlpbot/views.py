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
from nltk.stem.snowball import SnowballStemmer 
stemmer=SnowballStemmer("english")

from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# import spacy
# nlp=spacy.load('en_sm')

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
SlotSer=SlotService()
doctors=DocSer.getdoctors()

def doctorschat(intentval):
    # docname=getentities(ques)   department
    # intentval is department
    print(intentval)
    DocSer=DocService()
    if not intentval:
        doctors=DocSer.getdoctors()
        return doctors
    else:
        spec=stemmer.stem(intentval)
        # print(se )
        doctors=DocSer.getdocbydep(spec)
        return doctors
        # print(spec)
    

def slotschat(text):
    docname=getentities(text)
    matches=getdateandtime(text)
    while True:
        # get me all slots of doctor vijay on 20th November 10AM
        print(docname,matches)
        if docname:
            SlotSer=SlotService()
            msg=SlotSer.docslots(docname)
            print("Bot:"+str(msg))
            break
        elif not docname:
            print("Bot:Enter any doctor name")
            text=getinput()
            docname=getentities(text)
        # elif not matches:
        #     print("Bot:Enter date and time")
        #     text=getinput()
        #     matches=getdateandtime(text)
    print("Bot:Do you want to proceed for appointment?")
    confir=getinput()
    if confir=="yes":
        print("Bot:select time for the appointment")
        matches=getinput()
        msg=appointmentchat(str(docname)+" "+"on"+" "+str(matches))
    else:
        msg="Ok,Do you want see another doctor?"
    return (msg)

def appointmentchat(text):
    docname=getentities(text)
    print(docname)
    start_time=getdateandtime(text)
    print(docname,start_time)
    while True:
        if docname and start_time:
            # start_time=matches[0]
            if datetime.now()>start_time:
                print("Bot:Appointment not created,select from other timings")
            else:
                userday=str(start_time).split(" ")[0]
                usertime=start_time.strftime('%H:%M')
                appser=AppService()
                msg=appser.bookappointment(docname,usertime,"Y",userday,"srinu",text)
                return msg
        elif not docname:
            print("Bot:Enter any doctor name")
            text=getinput()
            docname=getentities(text)
        elif not start_time:
            print("Bot:Enter date and time")
            text=getinput()
            start_time=getdateandtime(text)      


# **************************
def getentities(text):
    doctor_name=""
    r=st.tag(text.title().split())
    for tag, chunk in groupby(r, lambda x:x[1]):
        if tag== "PERSON":
            doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
            doctor_name=doctor[1]
    return doctor_name


def getdateandtime(text):
    matches=list(datefinder.find_dates(text))
    if not matches:
        return None
    else:
        return matches[0]

def getinput():
    text=input("User:")
    return text

# *****************************



while True:
    # print("User:")
    ques=getinput()
    intent_struc=getintent(ques)
    intent=intent_struc['intent']['name']
    print(intent)
    if intent=="goodbye":
        print("Bye")
        break
    elif intent=="doctors":
        intent_val=""
        if intent_struc['entities']:
            intent_val=intent_struc['entities'][0]['value']
            response=doctorschat(intent_val)
        else:
            response=doctorschat(intent_val)
    elif intent=="appointment":
        response=appointmentchat(ques)
    elif intent=="slots":
        response=slotschat(ques)
    # elif intent=="greet":

    print("Bot:"+str(response))
