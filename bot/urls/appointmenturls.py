from django.urls import path
from bot.views import appointmentviews

# addappointment = SnippetViewSet.addappointment({
#     'post':'addappointment'
#     })

# appointmentindex = SnippetViewSet.index({
#     'get': 'list'
# })

# cancelappointment = SnippetViewSet.cancelappointment({
#     'get': 'list'
# })

urlpatterns=[
path('',appointmentviews.index,name='index'),
path('add',appointmentviews.AppointmentView.as_view(),name='appointment'),
path('cancel',appointmentviews.cancelappointment,name='cancelappt'),

]
