from django.db import models

class Doctors(models.Model):
    
    def __init__(self,doc_id,doc_name,specialization):
        # self.doc_id=None
        self.doc_name=None
        self.specialization=None
    
    def setDocname(self,doc_name):
        self.doc_name=doc_name
    
    def setSpecilization(self,specilization):
        self.specialization=specilization

    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctors'