from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add_data_to_db

# Create your views here.
def test(request):
    add_data_to_db.delay()
    return HttpResponse("Done")
