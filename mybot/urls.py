
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('appointment/',include('bot.urls.appointmenturls')),
    path('doctor/',include('bot.urls.doctorurls')),
    path('patient/',include('bot.urls.patienturls')),
    path('bot/',include('nlpbot.urls')),
    path('admin/', admin.site.urls),
]
