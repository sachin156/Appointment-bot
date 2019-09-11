from django.db import connection

class BookingStatus():

    def __init__(self):
        # self.book_id=None  Auto  Increment 
        self.doc_id=None
        self.slot_id=None
        self.book_date=None
        self.status=None
        self.pat_id=None
        self.cursor=connection.cursor()

    def insert(self,docid,bookdate,status,patid):
        insert_stmt = (
        "INSERT INTO booking_status (doc_id,slot_id,book_date,status,pat_id) "
        "VALUES (%s, %s,%s, %s,%s)"
        )
        data = (docid,bookdate,status,patid)
        return self.cursor.execute(insert_stmt, data)
    
    # def getDoctors(self):
    #     select_stmt = "SELECT doc_name,specialization FROM doctors"
    #     self.cursor.execute(select_stmt)
    #     return self.cursor.fetchall()
    
    def delete(self,doc_name):
        delet_stmt="""DELETE from doctors where doc_name=%s"""
        doc_name=doc_name
        return self.cursor.execute(delet_stmt, (doc_name,))
    
    # def getdocbyname(self,doc_name):
    #     select_stmt="""SELECT from doctors where doc_name=%s"""
    #     doc_name=doc_name
    #     return self.cursor.execute(select_stmt,(doc_name,))
         
