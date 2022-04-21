from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Members
import json
# Create your views here.
def root(req):
    home = loader.get_template('index.html')
    return HttpResponse(home.render())

def read(req):
    return JsonResponse(
        list(
            Members.objects.all().values()
        ),
        safe=False
    )
def read_one(req,id):
    try:
        member = Members.objects.get(id=id)
        return JsonResponse(
            {
                "id":member.id,
                "firstname":member.firstname,
                "lastname":member.lastname
            }
        )
    except:
        return JsonResponse(
            {
                "msg":"member not found"
            }
        )

def create(req):
    body = json.loads(req.body)
    firstname = body['firstname']
    lastname = body['lastname']
    model = Members(firstname=firstname,lastname=lastname)
    model.save()
    return JsonResponse({
        "create":True
    })

def update(req,id):
    body = json.loads(req.body)
    member = Members.objects.get(id=id)
    if 'firstname' in list(body.keys()):
        member.firstname = body['firstname']
    if 'lastname' in list(body.keys()):
        member.lastname = body['lastname']
    member.save()
    return JsonResponse({
        "update":True
    })

def delete(req,id):
    try:
        member = Members.objects.get(id=id)
        member.delete()
        return JsonResponse({"delete":True})
    except:
        return JsonResponse({"msg":"member not found"})