from django.http import HttpResponse
from datetime import date

# Create your views here.

from classwork_app.models import Mom
from classwork_app.models import Child

def list_family(request):
    moms = Mom.objects.all()
    for mom in moms:
        print(mom.mom_first_name)
        print(mom.mom_last_name)
        print(mom.mom_phone_number)



    return HttpResponse("List Bands")


def index(request):
    return HttpResponse("Index Page")

