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
from intentclassification import getintent

logger=logging.getLogger(__name__)

# ***********
st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
# *************
def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")

@csrf_exempt
def NlpView(request):
    text=request.POST.get('appointtext')
    print(text)
    # tokenized_text = (word_tokenize(string.capwords(text)))
    intent=getintent(text)
    print(intent)
    # tokenized_text = (word_tokenize(text))
    # ner tagging 
    # classified_text = st.tag(tokenized_text)
    # # removing stop words 
    # stop_words= set(stopwords.words('english'))
    # filtered_sentence=[word for word in tokenized_text if word not in stop_words]
    # print(filtered_sentence)
    # # pos tagging..
    # print(nltk.pos_tag(tokenized_text))
    # print(classified_text)
    # sentence = set(text.split())

    # dico = {
    # 'dict1':{'book','appointment','doctor'},
    # 'dict2':{'list','get','all','doctors'},
    # 'dict3':{'list','all','slots','doctor','get'},
    # # 'dict4':{'list','all','cardiologists','get'}
    # }
    # results = {}
    
    # for key, words in dico.items():
    #     results[key] = len(words.intersection(sentence))
    # value=max(results.items(), key=operator.itemgetter(1))[0]
    # print(value)
    
    # # objs for service classes....
    # DocSer=DocService()
    # doctors=DocSer.getdoctors()

    # doctor=""
    # for tag, chunk in groupby(classified_text, lambda x:x[1]):
    #     if tag== "PERSON":
    #         doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
    #         docname=doctor[1].lower()
    # print(doctor)

    # if value=='dict3':
    #     if doctor:
    #         SlotSer=SlotService()
    #         msg=SlotSer.docslots(docname)
    #         return HttpResponse(msg)
    #     else:
    #         return HttpResponse("Select any doctor from the suggested:"+str(doctors))
            
    # if value=='dict2':
    #     return HttpResponse(doctors)

    # if value=='dict1':
    #     if doctor:
    #         matches=list(datefinder.find_dates(text))
    #         start_time=matches[0]
    #         userday=str(start_time).split(" ")[0]
    #         usertime=start_time.strftime('%H:%M')
    #         appser=AppService()
    #         # patient name
    #         msg=appser.bookappointment(docname,usertime,"Y",userday,"srinu",text)
    #         return HttpResponse(msg)
    #     else:
    #         return HttpResponse("Select any doctor from the suggested:"+str(doctors))
    



















