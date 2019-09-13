from django.db import connection

class Appointment():

    def __init__(self):
        # self.book_id=None  Auto  Increment 
        self.doc_id=None
        self.slot_id=None
        self.book_date=None
        self.status=None
        self.pat_id=None
        self.cursor=connection.cursor()

    def insert(self,docid,slotid,bookdate,status,patid):
        insert_stmt = (
        "INSERT INTO booking_status (doc_id,slot_id,book_date,status,pat_id) "
        "VALUES (%s, %s,%s, %s,%s)"
        )
        data = (docid,slotid,bookdate,status,patid)
        self.cursor.execute(insert_stmt, data)
        return self.cursor.lastrowid
    
    def delete(self,bookid):
        print(bookid)
        delet_stmt="""DELETE from booking_status where book_id=%s"""
        msg=self.cursor.execute(delet_stmt, (bookid,))
        return msg
