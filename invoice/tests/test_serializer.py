import pytest
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer
from invoice.factories import InvoiceFactory




@pytest.mark.django_db
class TestInvoiceSerializer:
    def test_invoice_serializer(self, company):
        invoice_data = {
            'amount': '100.00',
            'date_posted': timezone.now().date(),
            'company': company.id,
            'number': '1D4SDFSDF'
        }
        serializer = InvoiceSerializer(data=invoice_data)
        assert serializer.is_valid()
        invoice = serializer.save()

        assert str(invoice.amount) == '100.00'
        assert invoice.company == company

    def test_invoice_list(self, company):
        InvoiceFactory.create(amount='200.00', company=company)
        InvoiceFactory.create(amount='300.00', company=company)

        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        assert len(serializer.data) == 2

    def test_invalid_company_id(self):
        invoice_data = {
            'amount': '400.00',
            'date_posted': timezone.now().date(),
            'company': 9999  # Company ID that doesn't exist
        }
        serializer = InvoiceSerializer(data=invoice_data)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
