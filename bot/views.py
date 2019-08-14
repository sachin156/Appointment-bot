from django.shortcuts import render,redirect
from django.http import HttpResponse
from .events import getfuncval
from .models import Doctors,Slots,BookingStatus,Patients
from django.db import connection


from .servicebot.docservice import getdocbyname
from .servicebot.slotsser import slotscount,getslots,docslots
from .servicebot.appointmentservice import bookappointment
from .servicebot.patientser import getpatients

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import datefinder

logger=logging.getLogger(__name__)



def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")


@require_http_methods(["GET","POST"])
@csrf_exempt
def appointment(request):
    reply={}
    if request.method=='POST':
        newtext=request.POST.get('appointtext')
        matches=list(datefinder.find_dates(newtext))
        if len(matches)==0:
            logger.error("Error:No Date and time")
        else:
            start_time=matches[0]
            userday=str(start_time).split(" ")[0]
            usertime=start_time.strftime('%H:%M')

        if datetime.now()>start_time:
            logger.exception("Enter Valid Date and Time")

        logger.info("Information of doctor and patient")
        docname=request.POST.get('docname')
        patname=request.POST.get('patname')

        # call doctor service in docservice..
        doc=getdocbyname(docname)
        if doc=="":
            logger.error("Error:Doctor name not found")
            return HttpResponse("Appointment not created,Doctor name not found")
        else:
            doctor_id=doc.doc_id
            flag=0
            flag=slotscount(userday,usertime,doctor_id)
            if flag>0:
                logger.warning("Try other date and time")
                return HttpResponse("Appointment not created,select from other timings")
            else:
                slotid=getslots(usertime)
                bookappointment(doc,slotid,"Y",userday)
                getfuncval(newtext)
            return HttpResponse("Appointment in process, Thanks")
    else:
        reply['message']="Hi!! Book an Appointment"
        return render(request,"bot.html",{"response":reply})

@require_http_methods(["GET"])
# get all available doctors
def doctors(request):
    reply={}
    doctors=[]
    temp=getdoc()
    for doc in temp:
        doctors.append(doc.doc_name)
    return HttpResponse(doctors)

# get available slots by doctor name
@require_http_methods(["POST"])
@csrf_exempt
def slotsbydoc(request):
    if request.method=='POST':
        docname=request.POST.get('docname')
        # doctorid=docid(docname)
        doctors=getdocbyname()
        if doc=="":
            logger.error("Error:Doctor name not found")
            return HttpResponse("Appointment not created,Doctor name not found")
        else:
            newslots=[]
            slots=docslots(doctorid)
            for slot in slots:
                date=slot[0]
                time=slot[1]
                datetime=str(date)+","+time+";  "
                newslots.append(datetime)
            return HttpResponse(newslots)
    return HttpResponse("Doctor name")

@require_http_methods(["GET","POST"])
def doctorslots(request,docname):
    docname=docname
    doctors=getdocbyname()
    if doc=="":
        logger.error("Error:Doctor name not found")
        return HttpResponse("Appointment not created,Doctor name not found")
    else:
        newslots=[]
        slots=docslots(doctorid)
        if not slots:
            logger.warning("No available slots ,change doc?")
        for slot in slots:
            date=slot[0]
            time=slot[1]
            datetime=str(date)+","+time+";  "
            newslots.append(datetime)
        return HttpResponse(newslots)

def patients(request):
    allpatients=getpatients()
    patientdetails=[]
    for patient in allpatients:
        patientdetails.append(patient.name+""+str(patient.pid)+" ")
    return HttpResponse(patientdetails)
