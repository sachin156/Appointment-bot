# from bot.modelsdb.appointmentmodels import BookingStatus,Slots
# from bot.modelsdb.doctormodels import Doctors
# from bot.modelsdb.patientmodels import Patients
# from bot.models import Doctors,Slots,BookingStatus,Patients
# from bot.modelsA import Doctors,Patients
from bot.modelsdb.appointmentmodels import BookingStatus
# from bot.services.slotsservice import 
from .docservice import DocService
from .patientser import PatService
from django.db import connection

cursor=connection.cursor()

class AppService():

    def __init__(self):
        self.AppService=BookingStatus()
        self.DocSer=DocService()
        self.PatSer=PatService()

    def bookappointment(self,docname,usertime,status,userday,patname):
        docid=self.DocSer.getdocbyname(docname)
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
        return "Appointments created"
        # bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday,pat=pat)
        # bookstats.save()
        # return "Appointment created on:" + str(bookstats.book_date) + "with booking id:" + str(bookstats.book_id)

    # def getbookstatus(pid):
    #     patstatus=BookingStatus.objects.filter(pat=pid)
    #     return patstatus

    # def cancelappt(bookid):
    #     booking=BookingStatus.objects.get(book_id=bookid)
    #     booking.delete()
    #     return "Appointment cancelled"

    # def apptbydoc(docname):
    #     bookings=BookingStatus.objects.filter(doc_name=docname)
    #     return bookings

    # def getappointment(patname):
    #     # s.all())
    #     return "appointments"

