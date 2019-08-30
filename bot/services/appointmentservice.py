from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection

cursor=connection.cursor()


def bookappointment(doc,slotid,status,userday,pat):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday,pat=pat)
    bookstats.save()
    return "Appointment created on:" + str(bookstats.book_date) + "with booking id:" + str(bookstats.book_id)

def getbookstatus(pid):
    patstatus=BookingStatus.objects.filter(pat=pid)
    return patstatus

def cancelappt(patname,docname):
    patient=Patients.objects.get(name=patname)
    doctor=Doctors.objects.get(doc_name=docname)
    BookingStatus.objects.filter(pat=patient.pid,doc=doctor.doc_id).delete()
    return "Appointment cancelled"

def apptbydoc(docname):
    bookings=BookingStatus.objects.filter(doc_name=docname)
    return bookings

def slotscount(userday,usertime,doctor_id):
    cursor.execute("SELECT count(b.status) From booking_status b,slots s Where b.slot_id=s.slot_id and b.book_date=%s and s.slot_time=%s and doc_id=%s",[userday,usertime,doctor_id])
    records=cursor.fetchall()
    count=records[0][0]
    return count

def getslots(usertime):
    slots=Slots.objects.get(slot_time=usertime)
    return slots

def docslots(doctor_id):
    cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)",[doctor_id])
    slots=cursor.fetchall()
    return slots

def GetSlot(slotid):
    slots=Slots.objects.get(slot_id=slotid)
    return slots