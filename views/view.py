from django.http import HttpResponse
from dbmodels.model import *
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

def get(request):
    text = "<h1>welcome to my app number </h1>"
    return HttpResponse(text)

def parse_params(pms):
    return dict((i,j) for i,j in pms.iteritems())

@csrf_exempt
@require_http_methods(["GET"])
def unique(request, attr):
    return JsonResponse(Company._unique(attr, **parse_params(request.GET)))

@csrf_exempt
@require_http_methods(["GET"])
def filter(request):
    return JsonResponse(Company._filter(**parse_params(request.GET)))

@csrf_exempt
@require_http_methods(["DELETE"])
def delete(request, company_name):
    try:
        Company._delete(company_name)
        return JsonResponse({"success" : "Company address deleted successfully"})
    except CompanyDoesNotExists as ex:
        return JsonResponse({"error" : ex.message}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def update(request, company_name):
    try:
        return JsonResponse(Company._update(company_name,**json.loads(request.body)))
    except CompanyDoesNotExists as ex:
        return JsonResponse({"error" : ex.message}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    try:
        return JsonResponse(Company._create(**json.loads(request.body) ))
    except CompanyAlreadyExists as ex:
        return JsonResponse({"error" : ex.message}, status=400)

