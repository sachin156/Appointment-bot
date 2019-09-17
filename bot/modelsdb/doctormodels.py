from django.db import connection
       
class Doctors():

    def __init__(self):
        self.doc_id=None
        self.doc_name = None
        self.specialization =None
        self.cursor=connection.cursor()
         


        

