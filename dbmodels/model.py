from django.db import models
import django
from django.db.models import Count

class CompanyAlreadyExists(Exception):
    pass

class CompanyDoesNotExists(Exception):
    pass

def parse_filter_args(params):
    dct = {}
    for k,v in params.iteritems():
        if k.endswith("~"):
            dct[k.replace("~", "__icontains")] = v
        else:
            dct[k] = v
    return dct

class Company(models.Model):
    company_name = models.CharField(primary_key = True,max_length = 150)
    building_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    
    class Meta:
        db_table = "company"

    def to_dict(self):
        dt = self.__dict__.copy()
        dt.pop("_state")
        return dt

    @classmethod
    def _create(cls, company_name, **params):
        if cls.objects.filter(company_name = company_name).exists():
            raise CompanyAlreadyExists("The company name with {} is already exists in records".format(company_name))

        new_company = cls(
            company_name = company_name,
            **params
        )
        new_company.save()
        return new_company.to_dict()

    @classmethod
    def _update(cls, company_name, **params):
        if not cls.objects.filter(company_name = company_name).exists():
            raise CompanyDoesNotExists("The company name with {} is doesn't exists in records".format(company_name))
        new_company = cls(
            company_name = company_name,
            **params
        )
        new_company.save()
        return new_company.to_dict()

    @classmethod
    def _delete(cls, company_name):
        filt =cls.objects.filter(company_name = company_name)
        if not filt.exists():
            raise CompanyDoesNotExists("The company name with {} is doesn't exists in records".format(company_name))
        filt.delete()
        return True

    @classmethod
    def _unique(cls, attr_name, count = 1, condition_type = "gt"):
        res = cls.objects.values(attr_name)\
            .annotate( **{ "{}_count".format(attr_name) : Count(attr_name) })\
            .filter(**{"{}_count{}".format(attr_name, "" if condition_type == "eq" else "__"+condition_type) : int(count) }) 
        l = tuple(i for i in res)
        return {"data" : l}

    @classmethod
    def _filter(cls, **params):
        filt = cls.objects.filter(**parse_filter_args(params))
        return {"data" : [o.to_dict() for o in filt] }
