from bot.models import Doctors,Slots,BookingStatus


def bookappointment(doc,slotid,status,userday,pat):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday,pat=pat)
    bookstats.save()
    return "Appointment created"

def getbookstatus(pid):
    patstatus=BookingStatus.objects.get(pat=pid)
    return patstatus
