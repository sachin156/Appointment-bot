from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection

cursor=connection.cursor()

def getpatients():
    patientsall=Patients.objects.all()
    return patientsall

def getpatientbyname(patname):
    patients=getpatients()
    for pat in patients:
        if patname.lower()==(pat.name).lower():
            return pat
    return ""

def addpat(patname,contact):
    newpatient=Patients(name=patname,contact=contact)
    newpatient.save()
    return "Patient added with name;"+newpatient.name 

def delpat(patname):
    patient=Patients.objects.get(name=patname)
    BookingStatus.objects.filter(pat=patient.pid).delete()
    patient.delete()
    return "Patient record deleted"