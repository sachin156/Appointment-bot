from django.db import models

# Create your models here.

class Patients(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patients'


