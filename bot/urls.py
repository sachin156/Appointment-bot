from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('doctors',views.doctors,name='doctors'),
path('appointment',views.appointment,name='appointment'),
# path('slots',views.slots,name='slots'),
path('slotsbydoc',views.slotsbydoc,name='slotsbydoc')
]
