from django.contrib import admin
from .models import Hospital, Doctor
from onus_base.models import OnUsUser

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Doctor)
