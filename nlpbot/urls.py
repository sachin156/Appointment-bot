from django.urls import path
from .import views

urlpatterns=[
path('',views.NlpView.as_view(),name='nlpbot'),
# path('',views.as_view(),name='appointment'),
# path('',views.as_view(),name='index')
# path('index/',views.index,name='index')
]
