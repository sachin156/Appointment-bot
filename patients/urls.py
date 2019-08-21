from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('allpatients',views.allpatients,name='allpatients'),
path('newpatient',views.addpatient,name='newpatient'),
path('delpatient',views.delpatient,name='delpatient'),
path('patientstat',views.patientbookstatus,name='patientdetails'),
]
