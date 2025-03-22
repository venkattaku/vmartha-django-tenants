from django.views.generic import TemplateView
from hospitals.models import Doctor
from django_multitenant.utils import set_current_tenant, get_current_tenant

# Create your views here.

class DoctorView(TemplateView):
    template_name = "hospitals/index_doctor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # current_tenant can be stored as a SESSION variable when a user logs in.
        # This should be done by the app
        t = get_current_tenant()
        #set the tenant
        set_current_tenant(t);

        context['doctors'] = Doctor.objects.all()
        return context