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

# from .intentclassification import getintent
from .util import getdateandtime,getentities
from .appointmentchat import AppchatService


# *************************


class SlotchatService():

    def __init__(self):
        # DocSer=DocService()
        self.SlotSer=SlotService()
        self.appchatser=AppchatService()
        # doctors=DocSer.getdoctors()

    def getinput(self):
        text=input("User:")
        return text

# ****************************
    def slotschat(self,text):

        docname=getentities(text)
        matches=getdateandtime(text)
        if not matches:
            matches=date.today().strftime("%Y-%m-%d")
            # print(matches)
        else:
            matches=matches.strftime("%Y-%m-%d")
        while True:
            if docname and matches:
                msg=self.SlotSer.docslots(matches,docname)
                print("Bot:"+str(msg))
                break
            
            #*********
            if not docname:
                docname=self.appchatser.checkdocname()
                if docname is None:
                    return "Starting Over,"
            #**********
            
        print("Bot:Do you want to proceed for appointment (yes/no)?")
        confir=self.getinput()
        if confir=="yes":
            print("Bot:select time for the appointment")
            matches=self.getinput()
            msg=self.appchatser.appointmentchat(str(docname)+" "+str(matches))
        else:
            msg="Ok,Do you want to see another doctor?"
        return (msg)


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
