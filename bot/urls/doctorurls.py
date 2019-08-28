from django.urls import path
from bot.views import doctorviews

urlpatterns=[
path('',doctorviews.index,name='index'),
path('all',doctorviews.alldocs,name='alldocs'),
path('new',doctorviews.adddoctor,name='newdoc'),
path('del/<str:docname>/',doctorviews.deletedoctor,name='deldoc'),
path('slots/<str:docname>/',doctorviews.slotsbydoc,name='slotsbydoc'),
]
