from django.urls import path
from bot.views import doctorviews

urlpatterns=[
path('',doctorviews.index,name='index'),# main index of the doctor page
path('all',doctorviews.alldocs,name='alldocs'),  # get all docs 
path('new',doctorviews.adddoctor,name='newdoc'),# Add new doctor to db
path('del/<str:docname>/',doctorviews.deletedoctor,name='deldoc'),# delete the doc from db using doc name
path('slots/<str:docname>/',doctorviews.doctorslots,name='slotsbydoc'),# Get all the slots by doc name
]
