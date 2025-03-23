from hospitals.models import Doctor
from django_multitenant.utils import set_current_tenant, get_current_tenant
from django.views.generic import ListView
from django.contrib import messages

class DoctorView(ListView):
    model = Doctor
    template_name = "index_doctor.html"
    context_object_name = "doctors"

    def get_queryset(self):
        t = get_current_tenant()
        self.extra_context = {"current_tenant": t}
        set_current_tenant(t)
        return Doctor.objects.filter(hospital_id=t)  # No need to explicitly filter by tenant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)  # Merge extra_context
        return context