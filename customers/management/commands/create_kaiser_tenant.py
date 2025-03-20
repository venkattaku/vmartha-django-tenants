from django.core.management.base import BaseCommand
from customers.models import Client, Domain

class Command(BaseCommand):
    help = "Create the Kaiser tenant and its domain"

    def handle(self, *args, **kwargs):
        # Create the tenant
        tenant = Client.objects.create(
            schema_name='kaiser',
            name='Kaiser',
            description='Vital recordings dashboard for Kaiser patients'
        )
        tenant.save()

        # Create the domain for the tenant
        domain = Domain.objects.create(
            domain='kaiser.test.com',
            tenant=tenant,
            is_primary=True
        )
        domain.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Kaiser tenant and domain.'))