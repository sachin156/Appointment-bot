from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.calendarevents import getfuncval
from django.db import connection

from bot.services.appointmentservice import bookappointment,getbookstatus,cancelappt,slotscount,getslots,docslots,apptbydoc
from bot.services.docservice import getdocbyname
from bot.services.patientser import getpatientbyname
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
def addappointment(request):
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
            logger.exception("Exception:Enter Valid Date and Time")

        logger.info("Information of doctor and patient")
        docname=request.POST.get('docname')
        patname=request.POST.get('patname')

        # call doctor service in docservice..
        doc=getdocbyname(docname)
        pat=getpatientbyname(patname)
        if doc=="" or pat=="":
            logger.error("Error:Doctor or patient name not found")
            return HttpResponse("Appointment not created")
        else:
            doctor_id=doc.doc_id
            flag=0
            flag=slotscount(userday,usertime,doctor_id)
            if flag>0:
                logger.warning("Try other date and time")
                return HttpResponse("Appointment not created,select from other timings")
            else:
                slotid=getslots(usertime)
                bookappointment(doc,slotid,"Y",userday,pat)
                getfuncval(newtext)
            return HttpResponse("Appointment in process, Thanks")
    else:
        reply['message']="Hi!! Book an Appointment"
        return render(request,"bot.html",{"response":reply})


@require_http_methods(["POST"])
@csrf_exempt
def cancelappointment(request):
    patname=request.POST.get('patname')
    docname=request.POST.get('docname')
    msg=cancelappt(patname,docname)
    return HttpResponse(msg)


def getappbyday(request):
    return "all"
