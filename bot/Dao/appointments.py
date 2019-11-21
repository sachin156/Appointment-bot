from django.db import connection
from bot.modelsdb.appointmentmodels import Appointment

class AppointmentDao(Appointment):

    def insert(self,docid,slotid,bookdate,status,patid):
        insert_stmt = (
        "INSERT INTO booking_status (doc_id,slot_id,book_date,status,pat_id) "
        "VALUES (%s, %s,%s, %s,%s)"
        )
        data = (docid,slotid,bookdate,status,patid)
        self.cursor.execute(insert_stmt, data)
        return self.cursor.lastrowid
    
    def delete(self,bookid):
        delet_stmt="""DELETE from booking_status where book_id=%s"""
        msg=self.cursor.execute(delet_stmt, (bookid,))
        return msg
