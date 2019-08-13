from .models import Doctors,Slots,BookingStatus
# from .docservice import bookappointments

def bookappointment(doc,slotid,status,userday):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday)
    bookstats.save()
    return "Appointment created"
