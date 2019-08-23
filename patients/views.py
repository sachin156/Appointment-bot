from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BookingStatus,Patients
from django.db import connection

from .patientser import getpatients,getpatientbyname,addpat,delpat

from bot.appointmentservice import getbookstatus,GetSlot
# from bot.tempd.appointmentservice import getbookstatus,GetSlot
from doctors.docservice import getdocbyid
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import datefinder

logger=logging.getLogger(__name__)

def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Patients Page")

@require_http_methods(["GET"])
def allpatients(request):
    allpatients=getpatients()
    patientdetails=[]
    for patient in allpatients:
        patientdetails.append(patient.name+""+str(patient.pid)+" ")
    return HttpResponse(patientdetails)

@csrf_exempt
def addpatient(request):
    pname=request.POST.get('patname')
    contact=request.POST.get('contact')
    msg=addpat(pname,contact)
    return HttpResponse(msg)

@csrf_exempt
def delpatient(request):
    logger.info("deleting patient removes relevant info from booking status")
    patname=request.POST.get('patname')
    msg=delpat(patname)
    return HttpResponse(msg)

@csrf_exempt
def patientbookstatus(request):
    patname=request.POST.get('patname')
    pid=getpatientbyname(patname)
    logger.error(pid)
    patstats=getbookstatus(pid)
    info=""
    for pat in patstats:
        docname=getdocbyid(pat.doc_id)
        logger.error(pat.slot)
        slottime=GetSlot(pat.slot_id)
        info+="Name:"+patname+" "+"BookingId:"+str(pat.book_id)+" "+"Doctor:"+docname.doc_name+" "+"BookDate:"+str(pat.book_date)+" "+"Time:"+slottime.slot_time+"\n"
    return HttpResponse(info)
