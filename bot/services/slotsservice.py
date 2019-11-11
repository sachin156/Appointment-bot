from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection
from bot.Dao.slots import SlotsDao
from .docservice import DocService

class SlotService():
    
    def __init__(self):
        self.SlotMap=SlotsDao()
        self.DocSer=DocService()
    
    def getslots(self,usertime):
        # slots=Slots.objects.get(slot_time=usertime)
        slots=self.SlotMap.getslot(usertime)
        if not slots:
            return ""
        else:
            return slots[0][0]
        return slots
    
    def slotscount(self,userday,usertime,docid):
        slotid=self.getslots(usertime)
        count=self.SlotMap.slotscount(userday,slotid,docid)
        count=count[0][0]
        return count

    def docslots(self,docname):
        docid=self.DocSer.getdocbyname(docname)
        if docid=="":
            return "Select from suggested doctors"+str(self.DocSer.getdoctors())
        slots=self.SlotMap.docslots(docid)
        newslots=[]
        for slot in slots:
            date_time = slot[0].strftime("%m/%d/%Y")
            newslots.append([date_time,slot[1]])
        # if slots=="":
        return newslots

    # def GetSlot(self,slotid):
    #     slots=Slots.objects.get(slot_id=slotid)
    #     return slots