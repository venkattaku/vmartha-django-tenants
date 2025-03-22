from django.db import models
from django_multitenant.fields import *
from django_multitenant.mixins import TenantModelMixin
from django_multitenant.models import TenantModel

class Hospital(TenantModel, models.Model):
  name =  models.CharField(max_length=50)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=50)
  class TenantMeta:
    tenant_field_name = "id"

class Doctor(TenantModelMixin, models.Model):
  name = models.CharField(max_length=255)
  doctor_id = models.CharField(max_length=50, primary_key=True)
  description = models.TextField()
  email = models.CharField(max_length=50)
  hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
  class TenantMeta:
    tenant_field_name = "hospital_id"
  class Meta:
    unique_together = ["doctor_id", "hospital_id"]