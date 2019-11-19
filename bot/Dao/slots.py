from django.db import connection
from bot.modelsdb.slotmodels import Slots
from datetime import datetime
# datetime object containing current date and time

class SlotsDao(Slots):

    def __init__(self):
        # self.book_id=None  Auto  Increment 
        self.slot_id=None
        self.slot_time=None
        self.cursor=connection.cursor()
    
    def getslot(self,usertime):
        select_stmt = "SELECT slot_id FROM slots where slot_time=%s"
        self.cursor.execute(select_stmt,(usertime,))
        return self.cursor.fetchall()
    
    def slotscount(self,userday,slotid,docid):
        select_stmt="SELECT count(b.status) From booking_status b,slots s Where b.slot_id=%s and b.book_date=%s and doc_id=%s"
        self.cursor.execute(select_stmt,(slotid,userday,docid))
        records=self.cursor.fetchall()
        return records
    
    def docslots(self,doctor_id):
        # now = datetime.now()
        # print("now =", now)
        # # dd/mm/YY H:M:S
        # dt_string = now.strftime("%Y-%m-%d")
        # print("date", dt_string)   
        select_stmt="SELECT DISTINCT b.book_date,s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)"
        # # select_stmt=""
        # select_stmt="Select DISTINCT s.slot_time FROM slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and select b.book_date s.slot_id not in(SELECT slot_id FROM booking_status where doc_id=%s)"
        self.cursor.execute(select_stmt,(doctor_id,))
        slots=self.cursor.fetchall()
        return slots
        
