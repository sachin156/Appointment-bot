# from bot.modelsdb.appointmentmodels import BookingStatus,Slots
# from bot.modelsdb.doctormodels import Doctors
# from bot.modelsdb.patientmodels import Patients
from bot.models import Doctors,BookingStatus
from django.db import connection

cursor=connection.cursor()

def getdoctors():
    doctors=Doctors.objects.all()
    return doctors

def getdocbyname(docname):
    doctors=getdoctors()
    for doc in doctors:
        if docname.lower()==(doc.doc_name).lower():
            return doc
    return ""

def getdocbyid(docid):
    doctors=getdoctors()
    for doc in doctors:
        if docid==doc.doc_id:
            return doc
    return ""

def createdoc(docname,spec):
    newdoc=Doctors(doc_name=docname,specialization=spec)
    newdoc.save()
    return "New doctor added with name:"+newdoc.doc_name

def deletedoc(docname):
    doctor=Doctors.objects.get(doc_name=docname)
    if not doctor:
        return "No doctor found"
    BookingStatus.objects.filter(doc=doctor.doc_id).delete()
    doctor.delete()
    return "doctor deleted"

def docslots(doctor_id):
    cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)",[doctor_id])
    slots=cursor.fetchall()
    return slots
