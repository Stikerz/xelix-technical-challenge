import random
import string

import factory
from factory.fuzzy import FuzzyAttribute

from .models import Invoice, Company


def generate_serial():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(3, 8)))


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("pystr", min_chars=4, max_chars=36)
    number = FuzzyAttribute(generate_serial)
    supplier_reference = factory.Faker("pystr", min_chars=4, max_chars=4)


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    number = FuzzyAttribute(generate_serial)
    amount = factory.Faker("pydecimal", right_digits=2, min_value=1, max_value=10000)
    date_posted = factory.Faker("date_between", start_date='-1y', end_date='today')
    company = factory.SubFactory(CompanyFactory)

