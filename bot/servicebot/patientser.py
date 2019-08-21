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

def addpatient(patname,number):
    newpatient=Doctors(name=patname,contact=number)
    newpatient.save()

def deletepatient(patname):
    patient=Patients.objects.get(name=patname)
    BookingStatus.objects.filter(pat=patient.name).delete()
    patinet.delete()
    return "Patient record deleted"
