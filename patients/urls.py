from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('allpatients',views.allpatients,name='allpatients'),
path('newpatient',views.addpatient,name='newpatient'),
path('delpatient',views.delpatient,name='delpatient'),
path('patientstat',views.patientbookstat,name='patientdetails'),
path('patientstatus/<slug:patname>/',views.patientbookstatus,name='patientstat'),
]
