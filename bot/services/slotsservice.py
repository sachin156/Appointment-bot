from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection
from bot.Dao.slots import SlotsDao

class SlotService():
    
    def __init__(self):
        self.SlotMap=SlotsDao()
    
    def getslots(self,usertime):
        # slots=Slots.objects.get(slot_time=usertime)
        slots=self.SlotMap.getslot(usertime)
        if not slots:
            return ""
        else:
            return slots[0][0]
        return slots
    
    def slotscount(self,userday,usertime,docid):
        count=self.SlotMap.slotscount(userday,usertime,docid)
        count=count[0][0]
        return count

    def docslots(self,doctor_id):
        # cursor.execute("SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)",[doctor_id])
        # slots=cursor.fetchall()
        slots=self.SlotMap.docslots(doctor_id)
        newslots=[]
        for slot in slots:
            date_time = slot[0].strftime("%m/%d/%Y")
            newslots.append([date_time,slot[1]])
        # if slots=="":
        return newslots

    # def GetSlot(self,slotid):
    #     slots=Slots.objects.get(slot_id=slotid)
    #     return slots