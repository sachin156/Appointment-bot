from django.db import models


class BookingStatus(models.Model):
    book_id = models.AutoField(primary_key=True)
    doc = models.ForeignKey('Doctors', models.DO_NOTHING, blank=True, null=True)
    slot = models.ForeignKey('Slots', models.DO_NOTHING, blank=True, null=True)
    book_date = models.DateField()
    status = models.CharField(max_length=255, blank=True, null=True)
    pat = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_status'

class Doctors(models.Model):

    # def __init__(self,doc_name,specialization):
    #     # self.doc_id=None
    #     self.doc_name=None
    #     self.specialization=None
    #     self.doc_id=None
    
    # def setDocname(self,doc_name):
    #     self.doc_name=doc_name
    
    # def setSpecilization(self,specilization):
    #     self.specialization=specilization

    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctors'


class Patients(models.Model):
    # def __init__(self,name,contact):
    #     self.name=name
    #     self.contact=contact
    
    # def setPatname(self,name):
    #     self.name=name
    
    # def setSpecilization(self,contact):
    #     self.contact=contact

    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
   
    class Meta:
        managed = False
        db_table = 'patients'

class Slots(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    slot_time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'slots'

