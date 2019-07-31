from django.shortcuts import render
from django.http import HttpResponse
from .events import getfuncval


def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    print(reply['message'])
    return render(request,"bot.html",{"response":reply})

def getappointment(request):
    reply={}
    if request.method=='POST':
        newtext=request.POST.get('appointtext')
        print(newtext)
        reply['message']=getfuncval(newtext)
        return render(request,"bot.html",{"response":reply})
    else:
        reply['message']="Hi!! Book an Appointmentalue"
        print(reply['message'])
        return render(request,"bot.html",{"response":reply})
