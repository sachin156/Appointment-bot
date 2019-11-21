from django.db import connection
from bot.modelsdb.slotmodels import Slots

# datetime object containing current date and time

class SlotsDao(Slots):
    
    def getslot(self,usertime):
        select_stmt = "SELECT slot_id FROM slots where slot_time=%s"
        self.cursor.execute(select_stmt,(usertime,))
        return self.cursor.fetchall()
    
    def slotscount(self,userday,slotid,docid):
        select_stmt="SELECT count(b.status) From booking_status b,slots s Where b.slot_id=%s and b.book_date=%s and doc_id=%s"
        self.cursor.execute(select_stmt,(slotid,userday,docid))
        records=self.cursor.fetchall()
        return records
        
    def docslots(self,app_dates,doctor_id):
        avail_slots=[]
        # print(app_dates)
        for app_date in app_dates:
            select_stmt="SELECT DISTINCT s.slot_time from slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(select slot_id from booking_status where book_date=%s and doc_id=%s)"
            self.cursor.execute(select_stmt,(app_date,doctor_id))
            slots=self.cursor.fetchall()
            avail_slots.append(slots)
        # print(avail_slots)
        return avail_slots



