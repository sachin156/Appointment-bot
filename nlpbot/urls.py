from django.urls import path
from .import views

urlpatterns=[
# path('',views.NlpView,name='nlpbot'),
path('index/',views.index,name='index')
]
