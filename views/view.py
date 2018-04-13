from django.http import HttpResponse
from dbmodels.model import Company
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def get(request):
    text = "<h1>welcome to my app number </h1>"
    return HttpResponse(text)


def parse_params(pms):
    return dict((i,j) for i,j in pms.iteritems())

@require_http_methods(["GET"])
def unique(request, attr):
    return JsonResponse(Company._unique(attr, **parse_params(request.GET)))


@require_http_methods(["GET"])
def filter(request):
    return JsonResponse(Company._filter(**parse_params(request.GET)))

@require_http_methods(["POST"])
def delete(request, company_name):
    return HttpResponse(Company._delete(company_name))

@require_http_methods(["POST"])
def update(request, company_name):
    return HttpResponse(Company._update(company_name, **parse_params(request.POST) ))

@require_http_methods(["POST"])
def create(request):
    return HttpResponse(Company._update(**parse_params(request.POST) ))

