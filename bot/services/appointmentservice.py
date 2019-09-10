# from bot.modelsdb.appointmentmodels import BookingStatus,Slots
# from bot.modelsdb.doctormodels import Doctors
# from bot.modelsdb.patientmodels import Patients
from bot.models import Doctors,Slots,BookingStatus,Patients
# from bot.modelsA import Doctors,Patients
from django.db import connection

cursor=connection.cursor()


def bookappointment(doc,slotid,status,userday,pat):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday,pat=pat)
    bookstats.save()
    return "Appointment created on:" + str(bookstats.book_date) + "with booking id:" + str(bookstats.book_id)

def getbookstatus(pid):
    patstatus=BookingStatus.objects.filter(pat=pid)
    return patstatus

def cancelappt(bookid):
    booking=BookingStatus.objects.get(book_id=bookid)
    booking.delete()
    return "Appointment cancelled"

def apptbydoc(docname):
    bookings=BookingStatus.objects.filter(doc_name=docname)
    return bookings

def getbookings():
    return "bookings"

# class apppointment():
