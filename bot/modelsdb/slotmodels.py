from django.db import connection
cursor=connection.cursor()

class Slots():

    def __init__(self): 
        self.slot_id=None
        self.slot_time=None
        self.cursor=connection.cursor()

