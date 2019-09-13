from django.urls import path
from bot.views import doctorviews

urlpatterns=[
path('',doctorviews.DoctorView.as_view(),name='index'),
path('delete/<str:docname>/',doctorviews.DoctorView.as_view(), name='delete_event'),

]
