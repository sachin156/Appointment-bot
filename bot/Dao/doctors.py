from django.db import connection
from bot.modelsdb.doctormodels import Doctors
       
class DoctorsDao(Doctors):
    
    def insert(self,docname,specialization):
        insert_stmt = (
        "INSERT INTO doctors (doc_name, specialization) "
        "VALUES (%s, %s)"
        )
        data = (docname,specialization)
        return self.cursor.execute(insert_stmt, data)
    
    def getDoctors(self):
        select_stmt = "SELECT doc_name,specialization FROM doctors"
        self.cursor.execute(select_stmt)
        return self.cursor.fetchall()
    
    def delete(self,doc_name):
        delet_stmt="""DELETE from doctors where doc_name=%s"""
        doc_name=doc_name
        return self.cursor.execute(delet_stmt, (doc_name,))
    
    def getdocbyname(self,doc_name):
        select_stmt="""SELECT doc_id from doctors where doc_name=%s"""
        self.cursor.execute(select_stmt,(doc_name,))
        return self.cursor.fetchall()
         


        

