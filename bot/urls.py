from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('appointment',views.getappointment,name='appointment'),
path('getdoctors',views.getdoctors,name='doctors'),
path('addappointment',views.addappointment,name='addappointment'),
path('getname',views.get_name,name='getname'),
path('getslots',views.getslots,name='getslots'),
path('slotsbydoc',views.slotsbydoc,name='slotsbydoc')
]
