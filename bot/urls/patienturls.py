from django.urls import path
from bot.views import patientviews

urlpatterns=[
path('',patientviews.index,name='index'),
path('all',patientviews.allpatients,name='allpatients'),
path('new',patientviews.addpatient,name='newpatient'), # Post Data to create new patient
path('del/<str:patname>/',patientviews.delpatient,name='delpatient'),
path('patientstatus/<str:patname>/',patientviews.patientbookstatus,name='patientstat'),
]
