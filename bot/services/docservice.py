from bot.models import Doctors,Slots,BookingStatus,Patients
from bot.modelsdb.doctormodels import Doctors
from django.db import connection
cursor=connection.cursor()


class DocService():

    def __init__(self):
        self.DocMap=Doctors()
        

    def createdoc(self,docname,spec):
        # newdoc=Doctors(doc_name=docname,specialization=spec)
        # newdoc.save()
        msg=self.DocMap.insert(docname,spec)
        return msg
        
    def getdoctors(self):
        doctors=self.DocMap.getDoctors()
        # records=doctors.fetchall()
        print(doctors)
        return doctors

    def deletedoc(self,docname):
        msg=self.DocMap.delete(docname)
        # doctor=Doctors.objects.get(doc_name=docname)
        # if not doctor:
        #     return "No doctor found"
        # BookingStatus.objects.filter(doc=doctor.doc_id).delete()
        # doctor.delete()
        return msg

    def getdocbyname(self,docname):
        msg=self.DocMap.getdocbyname(docname)
        print(msg)
        # doctors=getdoctors()
        # for doc in doctors:
        #     if docname.lower()==(doc.doc_name).lower():
        #         return doc
        return ""

    # def getdocbyid(self,docid):
    #     doctors=getdoctors()
    #     for doc in doctors:
    #         if docid==doc.doc_id:
    #             return doc
    #     return ""

    

    # def docslots(self,doctor_id):
    #     cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)",[doctor_id])
    #     slots=cursor.fetchall()
    #     return slots
