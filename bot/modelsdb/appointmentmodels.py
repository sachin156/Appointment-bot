from django.db import models

# Create your models here.

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


class Slots(models.Model):
    slot_id = models.IntegerField(primary_key=True)
    slot_time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'slots'
