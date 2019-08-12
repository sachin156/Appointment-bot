from django.db import models

# Create your models here.
class Doctors(models.Model):
    doc_id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=20)
    specialization = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctors'

class BookingStatus(models.Model):
    book_id = models.AutoField(primary_key=True)
    doc = models.ForeignKey('Doctors', models.DO_NOTHING, blank=True, null=True)
    slot = models.ForeignKey('Slots', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=3)
    book_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'booking_status'


class Patients(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patients'


class Scheduling(models.Model):
    pid = models.ForeignKey(Patients, models.DO_NOTHING, db_column='pid', blank=True, null=True)
    field_date = models.DateField(db_column='_date')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'scheduling'


class Slots(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    slot_time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'slots'
