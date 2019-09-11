from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

from bot.services.docservice import DocService
from bot.services.slotsservice import slotscount,getslots,docslots
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


# @require_http_methods(["GET","POST"])
# def doctorslots(request,docname):
#     docname=docname
#     doc=getdocbyname(docname)
#     if doc=="":
#         logger.error("Error:Doctor name not found")
#         return HttpResponse("Doctor name not found")
#     else:
#         newslots=[]
#         slots=docslots(doc.doc_id)
#         if not slots:
#             logger.warning("No available slots ,change doc?")
#         for slot in slots:
#             date=slot[0]
#             time=slot[1]
#             datetime=str(date)+","+time+";  "
#             newslots.append(datetime)
#         return HttpResponse(newslots)

# @require_http_methods(["DELETE"])
# @csrf_exempt
# def deletedoctor(request,docname):
#     logger.info("delete doctor removes all the information regarding doctor from booking_status")
#     # docname=request.POST.get("docname")
#     msg=deletedoc(docname.lower())
#     return HttpResponse(msg)
