from django.db import connection
       
class Patients():

    def __init__(self):
        self.name = None
        self.contact =None
        self.email=None
        self.cursor=connection.cursor()



        

