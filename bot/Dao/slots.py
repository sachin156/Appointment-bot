from django.db import connection
from bot.modelsdb.slotmodels import Slots

class SlotsDao(Slots):
    
    def getslot(self,usertime):
        select_stmt = "SELECT slot_id FROM slots"
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()
    
    def slotscount(self,userday,usertime,docid):
        print(userday,usertime,docid)
        select_stmt="SELECT count(b.status) From booking_status b,slots s Where b.slot_id=s.slot_id and b.book_date=%s and doc_id=%s"
        self.cursor.execute(select_stmt,(userday,docid))
        records=self.cursor.fetchall()
        print(records)
        return records
    
    def docslots(self,doctor_id):
        select_stmt="SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)"
        self.cursor.execute(select_stmt,(doctor_id,))
        slots=self.cursor.fetchall()
        return slots
        
