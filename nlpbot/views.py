from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import datefinder

from nltk.tag import StanfordNERTagger
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

logger=logging.getLogger(__name__)


st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
# stanford_classifier=""
# st=StanfordNERTagger(stanford_classifier)
def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")


@csrf_exempt
# Create your views here.
def NlpView(request):
    newtext=request.POST.get('appointtext')
    # tokenized_text = word_tokenize(newtext)
    # print(tokenized_text)
    classified_text = st.tag(newtext.split())
    print(classified_text)
    return HttpResponse(classified_text)
