from django.db import connection

class Appointment():

    def __init__(self):
        self.book_id=None  
        # Auto  Increment 
        self.doc_id=None
        self.slot_id=None
        self.book_date=None
        self.status=None
        self.pat_id=None
        self.cursor=connection.cursor()

   