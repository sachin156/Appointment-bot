# from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta,date
import logging
import datefinder
from itertools import groupby

from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService
from .intentclassification import getintent
from .util import getdateandtime,getentities


logger=logging.getLogger(__name__)


class AppchatService():
    
    def __init__(self):
        # DocSer=DocService()
        self.appser=AppService()
        # SlotSer=SlotService()
        # doctors=DocSer.getdoctors()

    def getinput(self):
        text=input("User:")
        return text

    def appointmentchat(self,text):
        docname=getentities(text)
        start_time=getdateandtime(text)
        # print(docname,start_time)
        while True:
            if docname and start_time:
                # start_time=matches[0]
                if datetime.now()>start_time:
                    print("Bot:Appointment not created,select from other timings")
                    text=self.getinput()
                    start_time=getdateandtime(text)   
                else:
                    print("Bot:Enter patient name")
                    patname=self.getinput()
                    userday=str(start_time).split(" ")[0]
                    usertime=start_time.strftime('%H:%M')
                    msg=self.appser.bookappointment(docname,usertime,"Y",userday,patname,text)
                    return msg
            elif not docname:
                print("Bot:Enter any doctor name")
                text=self.getinput()
                docname=getentities(text)
            elif not start_time:
                print("Bot:Enter date and time")
                text=self.getinput()
                start_time=getdateandtime(text)      



