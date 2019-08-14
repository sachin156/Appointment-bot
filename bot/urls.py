from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('doctors',views.doctors,name='doctors'),
path('appointment',views.appointment,name='appointment'),
path('slots',views.slotsbydoc,name='slotsbydoc'),
path('slotsbydoc/<slug:docname>/',views.doctorslots,name='slots'),
path('patients',views.patients,name='patients'),
]
