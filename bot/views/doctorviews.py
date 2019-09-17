from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
<<<<<<< HEAD
<<<<<<< HEAD

from bot.services.docservice import getdocbyname,getdocbyid,deletedoc,getdoctors,createdoc,docslots
=======
from bot.servicefold.docservice import getdocbyname,getdocbyid,deletedoc,getdoctors,createdoc,docslots
>>>>>>> d9351ad31fb6243b301f529ff1e89d93d55044aa
=======

<<<<<<< HEAD
from bot.services.docservice import getdocbyname,getdocbyid,deletedoc,getdoctors,createdoc
from bot.services.slotsservice import slotscount,getslots,docslots
>>>>>>> branch5bot
=======
from bot.services.docservice import DocService
# from bot.services.slotsservice import slotscount,getslots,docslots
>>>>>>> branch5bot
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import jsonify
import json
import datefinder
from rest_framework.views import APIView
from django.http import QueryDict

logger=logging.getLogger(__name__)

def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi,Doctor's Page")

<<<<<<< HEAD
@require_http_methods(["GET"])
# get all available doctors
def alldocs(request):
<<<<<<< HEAD
<<<<<<< HEAD
=======
    reply={}
>>>>>>> d9351ad31fb6243b301f529ff1e89d93d55044aa
=======
>>>>>>> branch5bot
    doctors=[]
    temp=getdoctors()
    # print(temp)
    for doc in temp:
        doctors.append(doc.doc_name+" ")
    return HttpResponse(doctors)
=======
class DoctorView(APIView):    
    
    def __init__(self):
        self.DocSer=DocService()

    def get(self,request,format=None):
        # doctors=[]
        temp=self.DocSer.getdoctors()
        return HttpResponse(temp)

    @csrf_exempt
    def post(self,request,format=None):
        docname=request.POST.get('docname')
        spec=request.POST.get('spec')
        msg=self.DocSer.createdoc(docname,spec)
        return HttpResponse(msg)
    
    def delete(self,request,docname,format=None):
        msg=self.DocSer.deletedoc(docname.lower())
        return HttpResponse(msg)
>>>>>>> branch5bot

