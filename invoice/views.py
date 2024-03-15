from rest_framework import viewsets, status
from rest_framework.response import Response
from invoice.models import Invoice, Company

from invoice.serializers import InvoiceSerializer, CompanySerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.models import F


class InvoiceViewSet(viewsets.ViewSet):

    def retrieve(self, request, number):
        invoice_instance = get_object_or_404(Invoice, number=number)
        serializer = InvoiceSerializer(invoice_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        supplier_reference = request.query_params.get('supplier_reference')
        if supplier_reference:
            queryset = Invoice.objects.filter(company__supplier_reference=supplier_reference)
        else:
            queryset = Invoice.objects.all()

        sorted_by = request.query_params.get('sorted_by', 'company_name')
        if sorted_by not in ['company_name', '-company_name', 'date_posted', '-date_posted']:
            raise ValidationError("Invalid value for 'sorted_by' parameter.")

        if sorted_by in ['company_name', '-company_name']:
            queryset = queryset.annotate(company_name=F('company__name')).order_by(sorted_by)
        elif sorted_by in ['date_posted', '-date_posted']:
            queryset = queryset.order_by(sorted_by)

        serializer = InvoiceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = InvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyViewSet(viewsets.ViewSet):

    def retrieve(self, request, supplier_reference):
        company_instance = get_object_or_404(Company, supplier_reference=supplier_reference)
        serializer = CompanySerializer(company_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)