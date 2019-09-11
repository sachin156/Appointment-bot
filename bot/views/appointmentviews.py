from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval
from django.db import connection

# from bot.services.appointmentservice import bookappointment,getbookstatus,getappointment,cancelappt,apptbydoc
from bot.services.slotsservice import slotscount,getslots,docslots
from bot.services.appointmentservice import AppService
# from bot.services.docservice import getdocbyname
# from bot.services.patientser import getpatientbyname
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import datefinder

from rest_framework.views import APIView
from django.http import QueryDict

logger=logging.getLogger(__name__)


def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi, Book an Appointment")

class AppointmentView(APIView):
    
    def __init__(self):
        self.AppSer=AppService()

    @csrf_exempt
    def post(self,request,format=None):
        # print(request.data.get('appointtext'))
        newtext=request.POST.get('appointtext')
        # logger.error(newtext)
        matches=list(datefinder.find_dates(newtext))
        if len(matches)==0:
            logger.error("Error:No Date and time")
        else:
            start_time=matches[0]
            userday=str(start_time).split(" ")[0]
            usertime=start_time.strftime('%H:%M')

        if datetime.now()>start_time:
            logger.exception("Exception:Enter Valid Date and Time")
            return HttpResponse("Appointment not created,select from other timings")

        # logger.info("Information of doctor and patient")
        docname=request.POST.get('docname')
        patname=request.POST.get('patname')

        # # call doctor service in docservice..
        # doc="getdocbyname(docname)"
        # pat="getpatientbyname(patname)"
        # if doc=="" or pat=="":
        #     logger.error("Error:Doctor or patient name not found")
        #     return HttpResponse("Appointment not created")
        # else:
        msg=self.AppSer.bookappointment(docname,usertime,"Y",userday,patname)
        # doctor_id=doc.doc_id
        # flag=0
        # flag=slotscount(userday,usertime,doctor_id)
        # if flag>0:
        #     logger.warning("Try other date and time")
        #     return HttpResponse("Appointment not created,select from other timings")
        # else:
        #     slotid=getslots(usertime)
        #     msg=bookappointment(doc,slotid,"Y",userday,pat)
        #     getfuncval(newtext)
        return HttpResponse(msg)
    
    # def get(self,request,patname,format=None):
    #     logger.info("Will fetch all the Appointments for the patient")
    #     print(patname.lower())
    #     msg=getappointment(patname.lower())
    #     # iterate over the msg 
    #     return HttpResponse(msg)
    
    # def delete(self,request,bookid,format=None):
    #     msg=cancelappt(bookid)
    #     return HttpResponse(msg)
        
# @require_http_methods(["POST"])
# @csrf_exempt
# def cancelappointment(request):
#     patname=request.POST.get('patname')
#     docname=request.POST.get('docname')
#     msg=cancelappt(patname,docname)
#     return HttpResponse(msg)
