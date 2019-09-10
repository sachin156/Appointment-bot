from django.db import models

class Doctors(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctors'


class Patients(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
   
    class Meta:
        managed = False
        db_table = 'patients'