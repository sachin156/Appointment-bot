from django.urls import path
from bot.views import patientviews

urlpatterns=[
path('',patientviews.PatientView.as_view(),name='patients'),
path('<str:patname>/',patientviews.PatientView.as_view(),name='delpatient'),
# path('status/<str:patname>/',patientviews.patientbookstatus,name='patientstat'),
]
