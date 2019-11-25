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
from .appointmentchat import AppchatService


# *************************


class SlotchatService():

    def __init__(self):
        # DocSer=DocService()
        self.SlotSer=SlotService()
        # appchatser=AppchatService()
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
        while True:
            # get me all slots of doctor vijay on 20th November 10AM
            # print(docname,matches)
            if docname and matches:
                msg=self.SlotSer.docslots(matches,docname)
                print("Bot:"+str(msg))
                break
            elif not docname:
                print("Bot:Enter any doctor name")
                text=self.getinput()
                docname=getentities(text)
            # elif not matches:
            #     print("Bot:Enter date and time")
            #     text=getinput()
            #     matches=getdateandtime(text)
        print("Bot:Do you want to proceed for appointment?")
        confir=self.getinput()
        if confir=="yes":
            print("Bot:select time for the appointment")
            matches=self.getinput()
            msg=self.appchatser.appointmentchat(str(docname)+" "+str(matches))
        else:
            msg="Ok,Do you want to see another doctor?"
        return (msg)

