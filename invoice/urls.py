from django.urls import path
from invoice.views import InvoiceViewSet, CompanyViewSet

urlpatterns = [
    path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
    path('invoices/<str:number>/', InvoiceViewSet.as_view({'get': 'retrieve'}), name='invoice-detail'),
    path('companies/<str:supplier_reference>/', CompanyViewSet.as_view({'get': 'retrieve'}), name='company-detail'),
]
