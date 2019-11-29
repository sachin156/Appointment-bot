from bot.models import Doctors,Slots,BookingStatus,Patients
from django.db import connection
from bot.Dao.slots import SlotsDao
from .docservice import DocService
from datetime import datetime,date,timedelta

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

    def docslots(self,appdate,docname):
        docid=self.DocSer.getdocbyname(docname)
        if docid=="":
            return "Select from suggested doctors"+str(self.DocSer.getdoctors())
        
        print(appdate)
        year=int(appdate.split('-')[0])
        month=int(appdate.split('-')[1])
        date=int(appdate.split('-')[2])

        date = datetime(year,month,date)
        app_dates=[]
        app_dates.append(appdate)
        for i in range(2):
            date +=timedelta(days=1)
            app_dates.append(date.strftime("%Y-%m-%d"))

        # slots=[]
        slots=self.SlotMap.docslots(app_dates,docid)
        newslots=[]

        # print(slots)
        index=0
        max_slots=0
        for slotdate in slots:
            for slot in slotdate:
                if max_slots>=10:
                    break
                date_time = app_dates[index]
                newslots.append([date_time,slot])
                max_slots+=1
            index+=1           
        return newslots

    # def GetSlot(self,slotid):
    #     slots=Slots.objects.get(slot_id=slotid)
    #     return slots

      # if slots: 
        #     for slot in slots:
        #         date_time = slot[0].strftime("%m/%d/%Y")
        #         newslots.append([date_time,slot[1]])
        # # if slots==""    :
