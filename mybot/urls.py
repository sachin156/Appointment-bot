
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('appointment',include('bot.urls.appointmenturls')),
    path('doctors/',include('bot.urls.doctorurls')),
    path('patients/',include('bot.urls.patienturls')),
    path('admin/', admin.site.urls),
]
