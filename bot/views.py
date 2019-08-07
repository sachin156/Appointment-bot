from django.shortcuts import render,redirect
from django.http import HttpResponse
from .events import getfuncval
from .models import Doctors,Slots,BookingStatus
from .forms import NameForm,contactForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import nltk

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop = stopwords.words('english')



def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")
    # return render(request,"bot.html",{"response":reply})

@csrf_exempt
def getappointment(request):
    reply={}
    doctor=['get all doctors','list all doctors','can you get all the doctors',
            'can you list all the doctors','list doctors']
    if request.method=='POST':
        # newtext=request.data
        newtext=request.POST.get('appointtext')
        # print(request.data)
        if newtext.lower() in doctor:
            return redirect('doctors')
        else:
            return redirect()
            # return redirect('addappointment')
            # reply=getfuncval(newtext)
            # print(reply)
            # reply['maintext']=newtext
            # # print(reply['decision'])
            # if reply['decision']=='True':
            #     return redirect('addappointment',response=reply['maintext'])
            # return render(request,"bot.html",{"response":reply})
    else:
        reply['message']="Hi!! Book an Appointment"
        return render(request,"bot.html",{"response":reply})


@csrf_exempt
def addappointment(request):

    reply={}
    doctor=['get all doctors','list all doctors','can you get all the doctors',
            'can you list all the doctors','list doctors']
    if request.method=='POST':
        newtext=request.POST.get('appointtext')
        print(newtext)
        if newtext.lower() in doctor:
            return redirect('doctors')
        else:
            # load stanford libraries to identify the person
            st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                                   '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
            r=st.tag(newtext.title().split())
            from itertools import groupby
            for tag, chunk in groupby(r, lambda x:x[1]):
                if tag== "PERSON":
                    doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
            doc_name=(doctor[1])


            doctors=Doctors.objects.all()
            for doc in doctors:
                if doc_name.lower()==(doc.doc_name).lower():
                    doctor_id=doc.doc_id
                    break
                else:
                    print("No doctor found")

            print(doctor_id)
            #  get booking status of the slots based on doc id
            bookingstats = BookingStatus.objects.raw('SELECT * FROM booking_status Where doc_id=%s',doctor_id)
            for person in bookingstats:
                print(person)
            reply={}
            reply['message']="Appointment in process, Thanks"
            return render(request,"bot.html",{"response":reply})
    else:
        reply['message']="Hi!! Book an Appointment"
        return render(request,"bot.html",{"response":reply})
    # print(response['maintext'])
    # print("called")


def getdoctors(request):
    reply={}
    doctors=[]
    temp=Doctors.objects.all()
    for doc in temp:
        doctors.append(doc.doc_name)
    # print(temp)
    # doctors= [doc.doc_name]
    return HttpResponse(doctors)
    # reply['message']="doctors: " +','.join(doctors)
    # return render(request,"bot.html",{"response":reply})


# this is just to know how forms are used..
def get_name(request):
    form={}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form['normal'] = NameForm(request.POST)
        form['contactform']=contactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponse('Thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form['normal'] = NameForm(request.POST)
        form['contactform']=contactForm(request.POST)

    return render(request, 'new.html', {'form': form})
