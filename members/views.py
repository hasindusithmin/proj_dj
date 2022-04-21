from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Members
# Create your views here.
def root(req):
    home = loader.get_template('index.html')
    return HttpResponse(home.render())

def get_member(req):
    return JsonResponse(
        list(
            Members.objects.all().values()
        ),
        safe=False
    )
