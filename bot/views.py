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

from django.db import connection

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
            import datefinder
            matches=list(datefinder.find_dates(newtext))
            if len(matches)==0:
                date_time=null
            else:
                start_time=matches[0]
                userday=str(start_time).split(" ")[0]
                usertime=start_time.strftime('%H:%M')

            print(userday)
            print(usertime)

            # load stanford libraries to identify the person
            st = StanfordNERTagger('/home/sachinv/Documents/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                                   '/home/sachinv/Documents/stanford-ner/stanford-ner.jar',encoding='utf-8')
            r=st.tag(newtext.title().split())
            from itertools import groupby
            for tag, chunk in groupby(r, lambda x:x[1]):
                if tag== "PERSON":
                    doctor=("%-12s"%tag, " ".join(w for w, t in chunk))
            doc_name=(doctor[1])

            print(doc_name)

            doctors=Doctors.objects.all()
            doctor_id=""
            for doc in doctors:
                if doc_name.lower()==(doc.doc_name).lower():
                    doctor_id=doc.doc_id
                    break
                else:
                    print("No doctor found")
            flag=0
            print(doctor_id)
            cursor=connection.cursor()
            if doctor_id!="":
                cursor.execute("SELECT count(b.status) From booking_status b,slots s Where b.slot_id=s.slot_id and b.book_date=%s and s.slot_time=%s and doc_id=%s",[userday,usertime,doctor_id])
                records=cursor.fetchall()
                flag=records[0][0]
                # SELECT count(b.status) FROM booking_status b,slots s Where b.slot_id=s.slot_id and s.slot_time=%s and b.doc_id=%s",[usertime],[doctor_id])
            print("flag",flag)
            if flag>0:
                return HttpResponse("Appointment not created select from other timings, Thanks")
            else:
                slotid=Slots.objects.get(slot_time=usertime)
                print(slotid.slot_id)
                print(doc.doc_id)
                bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday)
                bookstats.save()
            # print("flag",flag)
            # # get booking status of the slots based on doc id
            # reply={}
            # reply['message']="Appointment in process, Thanks"
            return HttpResponse("Appointment in process, Thanks")
            # return render(request,"bot.html",{"response":reply})
    else:
        reply['message']="Hi!! Book an Appointment"
        return render(request,"bot.html",{"response":reply})


# get all available doctors
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


# get slots of all available doctors
def getslots(request):
    cursor=connection.cursor()
    cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status)")
    slots=cursor.fetchall()
    print(type(slots))
    return HttpResponse(slots)
# this is just to know how forms are used..




def slotsbydoc(request):
    cursor=connection.cursor()
    cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=2)")
    slots=cursor.fetchall()
    newslots=[]
    for slot in slots:
        date=slot[0]
        time=slot[1]
        datetime=str(date)+","+time+";  "
        newslots.append(datetime)
    print(newslots)
    print(time)
    # newslots
    # for x,y in groupby(slots):

    # slotsby_doc=Manager.raw(select distinct s.slot_id,s.slot_time from slots s INNER JOIN booking_status b
    # on b.slot_id!=s.slot_id and s.slot_id not in(select slot_id from booking_status where doc_id=2));
    return HttpResponse(newslots)

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
