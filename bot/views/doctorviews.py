from django.shortcuts import render,redirect
from django.http import HttpResponse
from bot.calendarevents import getfuncval
from django.db import connection

from bot.services.docservice import getdocbyname,getdocbyid,deletedoc,getdoctors,createdoc
from bot.services.slotsservice import slotscount,getslots,docslots
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import logging
import jsonify
import json
import datefinder

logger=logging.getLogger(__name__)

def index(request):
    reply={}
    reply['message']="Hi!! Book an Appointment"
    return HttpResponse("Hi,Doctor's Page")

@require_http_methods(["GET"])
# get all available doctors
def alldocs(request):
    doctors=[]
    temp=getdoctors()
    # print(temp)
    for doc in temp:
        doctors.append(doc.doc_name+" ")
    return HttpResponse(doctors)

# get available slots by doctor name
# @require_http_methods(["POST"])
# @csrf_exempt
# def slotsbydoc(request):
#     if request.method=='POST':
#         docname=request.POST.get('docname')
#         # doctorid=docid(docname)
#         doc=getdocbyname(docname)
#         if doc=="":
#             logger.error("Error:Doctor name not found")
#             return HttpResponse("Doctor name not found")
#         else:
#             newslots=[]
#             slots=docslots(doc.doc_id)
#             for slot in slots:
#                 date=slot[0]
#                 time=slot[1]
#                 datetime=str(date)+","+time+";  "
#                 newslots.append(datetime)
#             return HttpResponse(newslots)
#     return HttpResponse("Doctor name")

@require_http_methods(["GET","POST"])
def doctorslots(request,docname):
    docname=docname
    doc=getdocbyname(docname)
    if doc=="":
        logger.error("Error:Doctor name not found")
        return HttpResponse("Doctor name not found")
    else:
        newslots=[]
        slots=docslots(doc.doc_id)
        if not slots:
            logger.warning("No available slots ,change doc?")
        for slot in slots:
            date=slot[0]
            time=slot[1]
            datetime=str(date)+","+time+";  "
            newslots.append(datetime)
        return HttpResponse(newslots)

@require_http_methods(["DELETE"])
@csrf_exempt
def deletedoctor(request,docname):
    logger.info("delete doctor removes all the information regarding doctor from booking_status")
    # docname=request.POST.get("docname")
    msg=deletedoc(docname.lower())
    return HttpResponse(msg)

@require_http_methods(["POST"])
@csrf_exempt
def adddoctor(request):
    # print(request.data['docname'])
    docname=request.POST.get('docname')
    spec=request.POST.get('spec')
    msg=createdoc(docname.lower(),spec)
    return HttpResponse(msg)
