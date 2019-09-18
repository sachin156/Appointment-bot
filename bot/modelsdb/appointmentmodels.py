from django.db import connection


# Each attribute represents a column name in the table
class Appointment():

    def __init__(self):
        self.book_id=None  # Auto  Increment 
        self.doc_id=None
        self.slot_id=None
        self.book_date=None
        self.status=None
        self.pat_id=None
        self.cursor=connection.cursor()

   