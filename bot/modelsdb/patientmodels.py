from django.db import connection
       
class Patients():

    def __init__(self):
        self.name = None
        self.contact =None
        self.cursor=connection.cursor()

    def insert(self,name,contact):
        insert_stmt = (
        "INSERT INTO patients (name, contact) "
        "VALUES (%s, %s)"
        )
        data = (name,contact)
        return self.cursor.execute(insert_stmt, data)
    
    def getPatients(self):
        select_stmt = "SELECT name,contact FROM patients"
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()
    
    def delete(self,name):
        delet_stmt="""DELETE from patients where name=%s"""
        name=name
        return self.cursor.execute(delet_stmt, (name,))
    
    def getpatbyname(self,patname):
        select_stmt="""SELECT pid from patients where name=%s"""
        self.cursor.execute(select_stmt,(patname,))
        return self.cursor.fetchall()


        

