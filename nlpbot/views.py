from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import string
import datefinder
from itertools import groupby
import operator

import nltk
from nltk.tag.stanford import StanfordNERTagger
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService

logger=logging.getLogger(__name__)


st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")

@csrf_exempt
def NlpView(request):
    text=request.POST.get('appointtext')
    tokenized_text = (word_tokenize(string.capwords(text)))
    classified_text = st.tag(tokenized_text)
    print(classified_text)
    sentence = set(text.split())

    dico = {
    'dict1':{'book','appointment','doctor'},
    'dict2':{'list','get','all','doctors'},
    'dict3':{'list','all','slots','doctor','get'}
    }
    results = {}
    
    for key, words in dico.items():
        results[key] = len(words.intersection(sentence))
    value=max(results.items(), key=operator.itemgetter(1))[0]
    print(value)
    
    if value=='dict3':
        for tag, chunk in groupby(classified_text, lambda x:x[1]):
            if tag== "PERSON":
                SlotSer=SlotService()
                doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
                print(doctor)
                msg=SlotSer.docslots(doctor[1].lower())
                return HttpResponse(msg)
    
    if value=='dict2':
        DocSer=DocService()
        docs=DocSer.getdoctors()
        return HttpResponse(docs)

    if value=='dict1':
        AppSer=AppService()
        # AppSer.bookappointment()
        # inputs of booking,doc,pat,time,slot
        return HttpResponse("Booking Appointment for you")




















