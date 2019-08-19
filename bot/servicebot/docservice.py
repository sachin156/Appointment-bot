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

def getdocbyid(docid):
    doctors=getdoctors()
    for doc in doctors:
        if docid==doc.doc_id:
            return doc
    return ""


def createdoc(docname,spec):
    bookstats=Doctors(doc_name=docname,specialization=spec)
    bookstats.save()

def deletedoc(docname):
    doctor=Doctors.objects.get(doc_name=docname)
    print(doctor)
    print(doctor.doc_id)
    bookstats=BookingStatus.objects.filter(doc=doctor.doc_id).delete()
    doctor.delete()
    return "doctor deleted"
