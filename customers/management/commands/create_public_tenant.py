from django.core.management.base import BaseCommand
from customers.models import Client, Domain

class Command(BaseCommand):
    help = "Create the Kaiser tenant and its domain"

    def handle(self, *args, **kwargs):
        # Create the public tenant
        public_tenant = Client.objects.create(
            schema_name='public',
            name='Public Tenant',
            description='Default public tenant'
        )
        public_tenant.save()

        # Create a domain for the public tenant
        domain = Domain.objects.create(
            domain='localhost',  # Replace with your domain if necessary
            tenant=public_tenant,
            is_primary=True
        )
        domain.save()

        self.stdout.write(self.style.SUCCESS('Successfully created public tenant and domain.'))


