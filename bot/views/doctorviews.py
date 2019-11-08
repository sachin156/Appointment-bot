from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

from bot.services.docservice import DocService
# from bot.services.slotsservice import slotscount,getslots,docslots
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

# def index(request):
    # reply={}
    # reply['message']="Hi!! Book an Appointment"
    # return HttpResponse("Hi,Doctor's Page")

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

