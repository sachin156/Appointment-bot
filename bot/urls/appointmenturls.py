from django.urls import path
from bot.views import appointmentviews

urlpatterns=[
path('',appointmentviews.index,name='index'),
path('appointment',appointmentviews.appointment,name='appointment'),
path('cancelappointment',appointmentviews.cancelappointment,name='cancelappt'),
# path('appbydoc',views.getappbydoc,name='cancelappt'),
]
