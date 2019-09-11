from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection
from bot.modelsdb.patientmodels import Patients
cursor=connection.cursor()


class PatService():
    
    def __init__(self):
        self.patmap=Patients()
    
    def getpatients(self):
        # patientsall=Patients.objects.all()
        patientsall=self.patmap.getPatients()
        return patientsall

    def addpat(self,patname,contact):
        newpatient=self.patmap.insert(patname,contact)
        if newpatient==1:
            return "Patient added with name:"+" "+patname
        else:
            return "Record Not added"

    def delpat(self,patname):
        # patient=Patients.objects.get(name=patname)
        # if not patient:
        #     return "No Patient found"
        # BookingStatus.objects.filter(pat=patient.pid).delete()
        # patient.delete()
        msg=self.patmap.delete([patname])
        if msg==1:
            return "Patinet with record name:"+patname+"deleted"
        else:
            return "Record not deleted."

    # def getpatientbyname(self,patname):
    #     patients=getpatients()
    #     for pat in patients:
    #         if patname.lower()==(pat.name).lower():
    #             return pat
    #     return "" 

  
