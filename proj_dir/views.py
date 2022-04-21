
from django.http import JsonResponse


def root(req):
    return JsonResponse({"msg":"Hello World"})