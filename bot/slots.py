from .models import Doctors,Slots,BookingStatus
from django.db import connection

def slotscount(userday,usertime,doctor_id):
    cursor=connection.cursor()
    cursor.execute("SELECT count(b.status) From booking_status b,slots s Where b.slot_id=s.slot_id and b.book_date=%s and s.slot_time=%s and doc_id=%s",[userday,usertime,doctor_id])
    records=cursor.fetchall()
    count=records[0][0]
    return count

def getslots(usertime):
    slots=Slots.objects.get(slot_time=usertime)
    return slots

def docslots(doctor_id):
    cursor=connection.cursor()
    print(doctor_id)
    cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)",[doctor_id])
    slots=cursor.fetchall()
    return slots




#\\\ef getdoc
