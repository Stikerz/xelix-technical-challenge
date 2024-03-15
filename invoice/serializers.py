from rest_framework import serializers

from invoice.models import Company, Invoice


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'number', 'supplier_reference']
        read_only_fields = ['id']


class InvoiceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Invoice
        fields = ['number', 'amount', 'date_posted', 'company']

    def to_representation(self, instance):
        """In the to_representation method, we dynamically set the CompanySerializer for the company field.
         This ensures that when serializing data to be returned in a response, the related company is serialized using
          the CompanySerializer, reducing the need for additional queries.
        """
        self.fields['company'] = CompanySerializer()  # Dynamically set CompanySerializer for company field
        return super().to_representation(instance)

    def to_internal_value(self, data):
        """In the to_internal_value method, we use PrimaryKeyRelatedField for the company field. This allows the serializer
         to accept the primary key of the company when creating or updating an invoice.

        """
        self.fields['company'] = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
        return super().to_internal_value(data)

    def create(self, validated_data):
        """In the create method, we extract the company ID from the provided data and use it to create the invoice.
         This avoids unnecessary queries for fetching the company object separately.
        """

        company = validated_data.pop('company')  # Extract company data
        invoice = Invoice.objects.create(company=company, **validated_data)  # Create invoice with existing company
        return invoice
