from django.db import connection
from bot.modelsdb.slotmodels import Slots
from datetime import datetime,date,timedelta
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
        
    def docslots(self,app_date,doctor_id):
        # if app_date=date.today().strftime("%Y-%m-%d"):

        # year=int(app_date.split('-')[0])
        # month=int(app_date.split('-')[1])
        # date=int(app_date.split('-')[2])

        # date = datetime(year,month,date)
        # app_dates=[]
        # for i in range(3): 
        #     date +=timedelta(days=1)
        #     app_dates.append(date.strftime("%Y-%m-%d") 

        select_stmt="SELECT DISTINCT s.slot_time from slots s INNER JOIN booking_status b on b.slot_id!=s.slot_id and s.slot_id not in(select slot_id from booking_status where book_date=%s and doc_id=%s)"
        self.cursor.execute(select_stmt,(app_date,doctor_id))
        slots=self.cursor.fetchall()
        print(slots)
        return slots