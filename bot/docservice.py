from .models import Doctors,Slots,BookingStatus
#
def getdoc():
    doctors=Doctors.objects.all()
    return doctors

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
