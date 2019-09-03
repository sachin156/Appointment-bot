from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

from bot.calendarevents import getfuncval
from bot.services.appointmentservice import getbookstatus
from bot.services.slotsservice import slotscount,getslots,docslots
from bot.services.docservice import getdocbyname,getdocbyid
from bot.services.patientser import getpatientbyname,getpatients,delpat,addpat

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

@require_http_methods(["POST"])
@csrf_exempt
def addpatient(request):
    pname=request.POST.get('patname')
    contact=request.POST.get('contact')
    msg=addpat(pname,contact)
    return HttpResponse(msg)

@require_http_methods(["DELETE"])
@csrf_exempt
def delpatient(request,patname):
    logger.info("deleting patient removes relevant info from booking status")
    msg=delpat(patname)
    return HttpResponse(msg)

@require_http_methods(["GET"])
@csrf_exempt
def patientbookstatus(request,patname):
    # patname=request.POST.get('patname')
    print(patname)
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
