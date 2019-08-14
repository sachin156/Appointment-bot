from bot.models import Doctors,Slots,BookingStatus
#
def getdoctors():
    doctors=Doctors.objects.all()
    return doctors

def getdocbyname(docname):
    doctors=getdoctors()
    for doc in doctors:
        if docname.lower()==(doc.doc_name).lower():
            return doc
    return ""

def createdoc(docname,spec):
    bookstats=Doctors(doc_name=docname,specialization=spec)
    bookstats.save()

# def docid(docname):
#     print(docname)
#     doctors=Doctors.objects.all()
#     doctorid=""
#     for doc in doctors:
#         if (doc.doc_name).lower()==docname.lower():
#             doctorid=doc.doc_id
#     return doctorid
