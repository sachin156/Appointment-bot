from django.urls import path
from .import views

urlpatterns=[
path('',views.index,name='index'),
path('alldocs',views.alldocs,name='alldocs'),
path('deletedoc',views.deletedoctor,name='deldoc'),
path('newdoc',views.adddoctor,name='newdoc'),
path('slots',views.slotsbydoc,name='slotsbydoc'),
path('slotsbydoc/<slug:docname>/',views.doctorslots,name='slots'),
]
