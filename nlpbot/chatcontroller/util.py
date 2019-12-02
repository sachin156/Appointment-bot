import datefinder
from itertools import groupby
import nltk
from nltk.stem.snowball import SnowballStemmer 
stemmer=SnowballStemmer("english")
from nltk.tag.stanford import StanfordNERTagger
from nltk.corpus import stopwords

jar='rasafiles/stanford-ner.jar'
model='rasafiles/english.all.3class.distsim.crf.ser.gz'


st = StanfordNERTagger(model,jar,encoding='utf-8')


def getinput():
    text=input("User:")
    return text

def getentities(text):
    doctor_name=None
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


def checkdocname():
    counter=0
    docname=None
    while counter<3: 
        print(counter)
        if docname is None:
            print("Bot:Enter doctor name")
            text=getinput()
            counter+=1
            docname=getentities(text)
        else:
            break
    return docname

def checkdate():
    counter=0
    start_time=None
    while counter<3: 
        if start_time is None:
            print("Bot:Enter date and time")
            text=getinput()
            counter+=1
            start_time=getdateandtime(text)
        else:
            break
    return start_time