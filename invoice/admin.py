from django.contrib import admin
from .models import Company, Invoice


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'supplier_reference')
    search_fields = ('name', 'number', 'supplier_reference')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'amount', 'date_posted', 'company')
    list_filter = ('date_posted', 'company')
    search_fields = ('number', 'company__name', 'company__supplier_reference')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('company')
        return queryset