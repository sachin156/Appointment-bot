from django.db import connection
from bot.modelsdb.patientmodels import Patients

class PatientsDao(Patients):

    def insert(self,name,contact,Email):
        insert_stmt = (
        "INSERT INTO patients (name, contact,email) "
        "VALUES (%s, %s,%s)"
        )
        data = (name,contact,Email)
        return self.cursor.execute(insert_stmt, data)
    
    def getPatients(self):
        select_stmt = "SELECT name,contact FROM patients"
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()
    
    def delete(self,name):
        delet_stmt="""DELETE from patients where name=%s"""
        return self.cursor.execute(delet_stmt, (name))
    
    def getpatbyname(self,patname):
        select_stmt="""SELECT pid from patients where name=%s"""
        self.cursor.execute(select_stmt,(patname,))
        return self.cursor.fetchall()


        

