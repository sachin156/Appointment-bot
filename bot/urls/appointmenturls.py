from django.urls import path
from bot.views import appointmentviews

urlpatterns=[
path('',appointmentviews.index,name='index'),
path('add',appointmentviews.addappointment,name='appointment'),
path('cancel',appointmentviews.cancelappointment,name='cancelappt'),
# path('getallby/<',appointmentviews.getappbyday,name='cancelappt'),
# path('appbydoc',views.getappbydoc,name='cancelappt'),
]
