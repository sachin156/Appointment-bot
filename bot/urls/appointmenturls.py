from django.urls import path
from bot.views import appointmentviews

urlpatterns=[
path('',appointmentviews.index,name='index'),
path('add',appointmentviews.AppointmentView.as_view(),name='appointment'),
path('cancel',appointmentviews.cancelappointment,name='cancelappt'),
]
