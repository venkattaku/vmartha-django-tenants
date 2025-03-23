from django.db import models
from django_multitenant.fields import *
from django_multitenant.mixins import TenantModelMixin, TenantManagerMixin
from django_multitenant.models import TenantModel

class HospitalManager(TenantManagerMixin, models.Manager):
  pass
class Hospital(TenantModel, models.Model):
  name =  models.CharField(max_length=50)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=50)
  tenant_id = "id"
  class TenantMeta:
    tenant_field_name = "id"

  def __str__(self):
    return self.name

class DoctorManager(TenantManagerMixin, models.Manager):
  pass
class Doctor(TenantModelMixin, models.Model):
  name = models.CharField(max_length=255)
  doctor_id = models.CharField(max_length=50, primary_key=True)
  description = models.TextField()
  email = models.CharField(max_length=50)
  hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
  tenant_id = "hospital_id"
  class TenantMeta:
    tenant_field_name = "hospital_id"
  class Meta:
    unique_together = ["doctor_id", "hospital"]
  def __str__(self):
    return self.name