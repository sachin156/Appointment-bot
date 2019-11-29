from bot.Dao.appointments import AppointmentDao
# from bot.services.slotsservice import 
from .docservice import DocService
from .patientser import PatService
from .slotsservice import SlotService
from .calendarevents import getfuncval
from django.db import connection
import logging 

import datefinder

logger=logging.getLogger(__name__)

cursor=connection.cursor()

class AppService():

    def __init__(self):
        self.BookMap=AppointmentDao()
        self.DocSer=DocService()
        self.PatSer=PatService()
        self.SlotSer=SlotService()

    def bookappointment(self,docname,usertime,status,userday,patname,newtext):
        # matches=list(datefinder.find_dates(newtext))
        # start_time=matches[0]
        # userday=str(start_time).split(" ")[0]
        # usertime=start_time.strftime('%H:%M')
        # appser=AppService()

        # print(docname,usertime,userday)
        doc_name=docname
        print("appointment",doc_name)
        # print(doc_name)
        docid=self.DocSer.getdocbyname(doc_name)
        patid=self.PatSer.getpatientbyname(patname)
        slotid=self.SlotSer.getslots(usertime)
        # ****

        if docid=="":
            return "Doctor Name Not Found,Select from the suggested"+str(self.DocSer.getdoctors())
        if patid=="":
            return "Patient Name Not Found"
        if slotid=="":
            return "Select from other timings"
        flag=0
        flag=self.SlotSer.slotscount(userday,usertime,docid)
        
        if flag>0:
            logger.warning("Try other date and time")
            slots=self.SlotSer.docslots(userday,doc_name)
            return "Appointment not created,select from other timings" +str(slots)
        else:
            msg=self.BookMap.insert(docid,slotid,userday,"Y",patid)
            # getfuncval(newtext)
            return "Appointment created with booking id:"+""+ str(msg)
       
    def getbookstatus(self,pid):
        # patstatus=self.BookMap.objects.filter(pat=pid)
        return "patstatus"

    def cancelappt(self,bookid):
        booking=self.BookMap.delete(bookid)
        if booking==1:
            return "Appointment deleted"
        # booking.delete()
        else:
            return "Check the booking id"
    #     bookings=BookingStatus.objects.filter(doc_name=docname)


