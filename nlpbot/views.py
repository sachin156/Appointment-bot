from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import datefinder

from nltk.tag import StanfordNERTagger
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService
from .intentclassification import getintent


logger=logging.getLogger(__name__)


st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
# stanford_classifier=""
# st=StanfordNERTagger(stanford_classifier)

logger=logging.getLogger(__name__)

# **************
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
    # get intent from rasa
    intent=getintent(text)

    tokenized_text = (word_tokenize(text.title()))
    # ner tagging 
    classified_text = st.tag(tokenized_text)

       # # objs for service classes....
    DocSer=DocService()
    doctors=DocSer.getdoctors()

    doctor=""
    for tag, chunk in groupby(classified_text, lambda x:x[1]):
        if tag== "PERSON":
            doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
            docname=doctor[1].lower()
   
    print(doctor)

    print("Intent of the sentence"+intent)
    if intent=='appointment':
        if doctor:
            matches=list(datefinder.find_dates(text))
            start_time=matches[0]
            userday=str(start_time).split(" ")[0]
            usertime=start_time.strftime('%H:%M')
            appser=AppService()
            # patient name
            msg=appser.bookappointment(docname,usertime,"Y",userday,"srinu",text)
            return HttpResponse(msg)
        else:
            return HttpResponse("Select any doctor from the suggested:"+str(doctors))

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
    
    if intent =='slots':
        if doctor:
            SlotSer=SlotService()
            msg=SlotSer.docslots(docname)
            return HttpResponse(msg)
        else:
            return HttpResponse("Select any doctor from the suggested:"+str(doctors))
            
    if intent=='doctors':
        return HttpResponse(doctors)









