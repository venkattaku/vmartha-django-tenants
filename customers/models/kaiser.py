from customers.models import Client, Domain

Client(schema_name='kaiser',
    name='Kaiser',
    description='Public Tenant').save()

Domain(domain='kaiser.test.com',
    tenant=Client.objects.get(schema_name='kaiser'),
    is_primary=False).save()