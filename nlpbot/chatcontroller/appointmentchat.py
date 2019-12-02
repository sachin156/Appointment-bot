# from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.services.calendarevents import getfuncval

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta,date
import logging
import datefinder
from itertools import groupby

from bot.services.patientser import PatService
from bot.services.slotsservice import SlotService
from bot.services.docservice import DocService
from bot.services.appointmentservice import AppService

# from .intentclassification import getintent
from .util import getdateandtime,getentities,checkdate,checkdocname


logger=logging.getLogger(__name__)


class AppchatService():
    
    def __init__(self):
        # DocSer=DocService()
        self.appser=AppService()
        self.patser=PatService()
        # SlotSer=SlotService()
        # doctors=DocSer.getdoctors()

    def getinput(self):
        text=input("User:")
        return text
    

    def patdetails(self):
        print("Bot:Are you Registered User(yes/no)")
        text=self.getinput()
        if text.lower()=="yes":
            print("Bot:Enter patient name")
            patname=self.getinput()
            return patname
        else:
            print("Bot:Enter patient name")
            patname=self.getinput()
            print("Bot:Phone Number")
            phonenumber=self.getinput()
            # passing null values to email id..
            self.patser.addpat(patname,phonenumber,"")
            return patname

    def appointmentchat(self,text):
        docname=getentities(text)
        start_time=getdateandtime(text)    
        # print(docname,start_time)
        while True:
            if docname and start_time:
                # start_time=matches[0]
                week_day=start_time.weekday()
                # print(week_day)
                if datetime.now()>start_time or week_day==6:
                    print("Bot:Appointment not created,select from other timings")
                    text=self.getinput()
                    start_time=getdateandtime(text)   
                else:
                    patname=self.patdetails()
                    userday=str(start_time).split(" ")[0]
                    usertime=start_time.strftime('%H:%M')
                    msg=self.appser.bookappointment(docname,usertime,"Y",userday,patname,text)
                    return msg
            

            #***********
            if not docname:
                docname=checkdocname()
                print(docname)
                if docname is None:
                    return "Starting Over,"
            
            if not start_time:
                start_time=checkdate()
                if start_time is None:
                    return "Starting Over,"
            
            #***********       
    

           



