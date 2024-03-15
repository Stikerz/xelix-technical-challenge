import pytest
from rest_framework import status
from django.urls import reverse
from invoice.factories import InvoiceFactory


@pytest.mark.django_db
class TestInvoiceViewSet:
    def test_retrieve(self, sample_invoice, api_client):
        response = api_client.get(reverse("invoice-detail", kwargs={"number": sample_invoice.number}))
        assert response.status_code == 200
        assert response.data.get('company').get('name') == sample_invoice.company.name

    def test_list(self, sample_invoice, api_client):
        response = api_client.get(reverse("invoice-list"))
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_list_sorted_by_date_posted(self, sample_invoice, company, api_client):
        # Create more invoices with different dates for sorting test
        InvoiceFactory.create(
            number='INV-002',
            amount=200.00,
            date_posted='2024-03-06',
            company=company
        )
        InvoiceFactory.create(
            number='INV-003',
            amount=300.00,
            date_posted='2024-03-04',
            company=company
        )

        response = api_client.get(reverse("invoice-list"), {'sorted_by': 'date_posted'})
        assert response.status_code == 200
        assert len(response.data) == 3
        # Check if sorting is correct
        assert response.data[0]['number'] == 'INV-003'
        assert response.data[2]['number'] == 'INV-002'

    def test_invalid_sorted_by_param(self, sample_invoice, api_client):
        response = api_client.get(reverse("invoice-list"), {'sorted_by': 'invaliddd'})
        assert response.status_code == 400
        assert response.json()[0] == "Invalid value for 'sorted_by' parameter."

    def test_create(self, api_client, company):
        request_data = {
            'number': 'INV-004',
            'amount': '400.00',
            'date_posted': '2024-03-07',
            'company': company.id
        }
        response = api_client.post(reverse("invoice-list"), request_data, format='json')
        assert response.status_code == 201


@pytest.mark.django_db
class TestCompanyViewSet:

    def test_retrieve_company(self, api_client, company):
        url = reverse('company-detail', args=[company.supplier_reference])
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json().get('name') == company.name
