# from bot.Dao.modelsdb. import Doctors,Slots,BookingStatus,Patients
from bot.Dao.doctors import DoctorsDao
from django.db import connection
cursor=connection.cursor()


class DocService():

    def __init__(self):
        self.DocMap=DoctorsDao()
        

    def createdoc(self,docname,spec):
        msg=self.DocMap.insert(docname,spec)
        return msg
        
    def getdoctors(self):
        doctors=self.DocMap.getDoctors()
        # records=doctors.fetchall()
        print(doctors)
        return doctors

    def deletedoc(self,docname):
        msg=self.DocMap.delete(docname)
        return msg

    def getdocbyname(self,docname):
        msg=self.DocMap.getdocbyname(docname)
        if msg:
            docid=msg[0][0]
            return docid
        else:
            return ""

 