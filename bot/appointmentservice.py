from .models import Doctors,Slots,BookingStatus,Patients


def bookappointment(doc,slotid,status,userday,pat):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday,pat=pat)
    bookstats.save()
    return "Appointment created"

def getbookstatus(pid):
    patstatus=BookingStatus.objects.filter(pat=pid)
    return patstatus

def cancelappt(patname,docname):
    patient=Patients.objects.get(name=patname)
    doctor=Doctors.objects.get(doc_name=docname)
    BookingStatus.objects.filter(pat=patient.pid,doc=doctor.doc_id).delete()
    return "Appointment canceled"

def apptbyday():
    return "apptbyday"
