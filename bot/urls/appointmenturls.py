from django.urls import path
from bot.views import appointmentviews

urlpatterns=[
# path('',appointmentviews.index,name='index'),
path('',appointmentviews.AppointmentView.as_view(),name='appointment'),
path('delete/<int:bookid>/',appointmentviews.AppointmentView.as_view(),name='cancelappt'),
]
