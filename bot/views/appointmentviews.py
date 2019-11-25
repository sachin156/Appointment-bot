from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

# from bot.services.appointmentservice import bookappointment,getbookstatus,getappointment,cancelappt,apptbydoc
# from bot.services.slotsservice import slotscount,getslots,docslots
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


# def index(request):
#     reply={}
#     reply['message']="Hi!! Book an Appointment"
#     return HttpResponse("Hi, Book an Appointment")

class AppointmentView(APIView):
    
    def __init__(self):
        self.AppSer=AppService()

    @csrf_exempt
    def post(self,request,format=None):
        # print(request.data.get('appointtext'))
        newtext=request.POST.get('appointtext')
        # logger.error(newtext)
        docname=request.POST.get('docname')
        # print(docname)
        patname=request.POST.get('patname')
        matches=list(datefinder.find_dates(newtext))
        if len(matches)==0:
            logger.error("Error:No Date and time")
            return HttpResponse("Appointment not created,select from other timings")
        else:
            start_time=matches[0]
            userday=str(start_time).split(" ")[0]
            usertime=start_time.strftime('%H:%M')
        if datetime.now()>start_time:
            logger.exception("Exception:Enter Valid Date and Time")
            return HttpResponse("Appointment not created,select from other timings")
        # print(datetime.now())
        # print(start_time)
        msg=self.AppSer.bookappointment(docname,usertime,"Y",userday,patname,newtext)
        return HttpResponse("pend")
    
    

    def delete(self,request,bookid,format=None):
        print(bookid)
        msg=self.AppSer.cancelappt(bookid)
        return HttpResponse(msg)
        