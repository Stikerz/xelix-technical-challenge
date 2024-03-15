
from invoice.models import Invoice
from rest_framework.test import APIRequestFactory, APIClient
from invoice.factories import CompanyFactory, InvoiceFactory
import pytest


@pytest.fixture
def company():
    return CompanyFactory.create(name="Test Company", number="12345")


@pytest.fixture()
def valid_invoice(company):
    return {
            'amount': 100.00,
            'date_posted': '2024-03-05',
            'company': company.id,
            'number': '1D4564F'
        }


@pytest.fixture
def sample_invoice(valid_invoice, company):
    return InvoiceFactory.create(
        number=valid_invoice.get("number"),
        amount=valid_invoice.get("gross_amount"),
        date_posted=valid_invoice.get("date_posted"),
        company=company
    )


@pytest.fixture
def request_factory():
    return APIRequestFactory()


@pytest.fixture
def api_client():
    return APIClient()