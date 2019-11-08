from django.urls import path
from .import views

urlpatterns=[
path('',views.NlpView,name='nlpview'),
]
