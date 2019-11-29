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
from .util import getdateandtime,getentities


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

    def appointmentchat(self,text):
        docname=getentities(text)
        start_time=getdateandtime(text)    
        print(docname,start_time)
        while True:
            # if start_time.weekday()==6:
            #     print("Bot:Doctor is available only on weekdays(Mon-Sat)")
            
            if docname and start_time:
                # start_time=matches[0]
                week_day=start_time.weekday()
                print(week_day)
                if datetime.now()>start_time and week_day!=6:
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
                docname=self.checkdocname()
                if docname is None:
                    return "Starting Over,"
            
            if not start_time:
                start_time=self.checkdate()
                if start_time is None:
                    return "Starting Over,"
            
            #***********       
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

    
    def checkdocname(self):
        counter=0
        docname=""
        while counter<3: 
            if not docname:
                print("Bot:Enter doctor name")
                text=self.getinput()
                counter+=1
                docname=getentities(text)
            else:
                return docname
        return None
            
    def checkdate(self):
        counter=0
        start_time=""
        while counter<3: 
            if not start_time:
                print("Bot:Enter date and time")
                text=self.getinput()
                counter+=1
                start_time=getdateandtime(text)
            else:
                return start_time
        return None

           



