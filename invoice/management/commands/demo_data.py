import random

from django.core.management.base import BaseCommand

from invoice.factories import InvoiceFactory, CompanyFactory
from invoice.models import Invoice, Company


class Command(BaseCommand):
    help = "Create a database full of made up test data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Deleting existing data"))
        Invoice.objects.all().delete()
        Company.objects.all().delete()

        self.stdout.write(self.style.NOTICE("Creating new demo data"))
        for supplier_reference in ['ALP1', 'BET1', 'CH1']:
            company = CompanyFactory.create(supplier_reference=supplier_reference)
            InvoiceFactory.create_batch(random.randint(1, 5), company=company)
        self.stdout.write(self.style.SUCCESS("Demo Data Create"))