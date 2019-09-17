from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
from bot.services.appointmentservice import getbookstatus,GetSlot
from bot.services.docservice import getdocbyname,getdocbyid
from bot.services.patientser import getpatientbyname,getpatients,delpat,addpat
=======
from bot.servicefold.appointmentservice import getbookstatus
from bot.servicefold.docservice import getdocbyname,getdocbyid
from bot.servicefold.patientser import getpatientbyname,getpatients,delpat,addpat
>>>>>>> d9351ad31fb6243b301f529ff1e89d93d55044aa
=======
=======
>>>>>>> branch5bot
from bot.services.calendarevents import getfuncval
from bot.services.patientser import PatService

>>>>>>> branch5bot
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
    return HttpResponse("Hi, Patients Page")

class PatientView(APIView):
    
    def __init__(self):
        self.PatSer=PatService()
    
    def get(self,request,format=None):
        allpatients=self.PatSer.getpatients()
        return HttpResponse(allpatients)

    @csrf_exempt
    def post(self,request,format=None):
        pname=request.POST.get('patname')
        contact=request.POST.get('contact')
        email=request.POST.get('Email')
        msg=self.PatSer.addpat(pname,contact,email)
        return HttpResponse(msg)
    
    def delete(self,request,patname,format=None):
        logger.info("deleting patient removes relevant info from booking status")
        msg=self.PatSer.delpat(patname.lower())
        return HttpResponse(msg)
        # msg=self.PatSer.delpat(patname)
        # return HttpResponse(msg)


# @require_http_methods(["GET"])
# @csrf_exempt
# def patientbookstatus(request,patname):
#     # patname=request.POST.get('patname')
#     print(patname)
#     pid=getpatientbyname(patname)
#     logger.error(pid)
#     patstats=getbookstatus(pid)
#     info=""
#     for pat in patstats:
#         docname="getdocbyid(pat.doc_id)"
#         logger.error(pat.slot)
#         slottime=GetSlot(pat.slot_id)
#         info+="Name:"+patname+" "+"BookingId:"+str(pat.book_id)+" "+"Doctor:"+docname.doc_name+" "+"BookDate:"+str(pat.book_date)+" "+"Time:"+slottime.slot_time+"\n"
#     return HttpResponse(info)
