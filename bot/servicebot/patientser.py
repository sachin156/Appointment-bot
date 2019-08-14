from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection

cursor=connection.cursor()

def getpatients():
    patientsall=Patients.objects.all()
    return patientsall

def getpatientid(docname):
    doctors=getpatients()
    doctor_id=""
    for doc in doctors:
        if docname.lower()==(doc.doc_name).lower():
            doctor_id=doc.doc_id
            break
    return doctor_id
