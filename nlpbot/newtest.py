from datetime import datetime, timedelta
import logging
import string
import re
import datefinder
from itertools import groupby
import operator

import nltk
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


import spacy
from spacy import displacy

import en_core_web_sm
nlp=en_core_web_sm.load()

logger=logging.getLogger(__name__)

# ***********
st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
# *************
# def index(request):
#     reply={}
#     reply['message']="Hi!! Book an Appointment"
#     return HttpResponse("Hi, Book an Appointment")


text=input("Enter the sentence")
tokenized_text = (word_tokenize(string.capwords(text)))
# ner tagging can 
classified_text = st.tag(tokenized_text)
# removing stop words 
stop_words= set(stopwords.words('english'))
filtered_sentence=[word for word in tokenized_text if word not in stop_words]
# print(filtered_sentence)
# pos tagging..
postag=nltk.pos_tag(filtered_sentence)
print(postag)
tags=[]
for i in range(len(postag)):
    tags.append(postag[i][1])
print("Tags",tags)
# print(classified_text)
sentence = set(text.split())


# temp="INNNPIN"

# for tag in tags:
#     if re.search(tag, temp, re.I):
#         print("The %s is within %s." % (list,temp))

for tag, chunk in groupby(classified_text, lambda x:x[1]):
    if tag== "PERSON":
        doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
        docname=doctor[1].lower()
        print(doctor)

matches=list(datefinder.find_dates(text))
if matches:
    start_time=matches[0]
    # print(start_time)
# else:
#     print("Time and Day")



# using spacy library for grammar

doc = nlp(text.title())
# print([(X.text, X.label_) for X in doc.ents])
# print([(X, X.ent_iob_, X.ent_type_) for X in doc])

# for token in doc:
    # print(token,token.pos_, token.tag_)


















