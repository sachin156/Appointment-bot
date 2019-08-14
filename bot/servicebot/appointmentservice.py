from bot.models import Doctors,Slots,BookingStatus


def bookappointment(doc,slotid,status,userday):
    bookstats=BookingStatus(doc=doc,slot=slotid,status='Y',book_date=userday)
    bookstats.save()
    return "Appointment created"
