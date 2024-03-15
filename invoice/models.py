from django.db import models


class Company(models.Model):
    """ Model representing Supplier Company. """
    name = models.CharField(max_length=36)
    number = models.CharField(max_length=36)
    supplier_reference = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """ Model representing an invoice. """


    number = models.CharField(max_length=36, unique=True)
    amount = models.DecimalField("Total Invoice Amount",
                                 decimal_places=2,
                                 max_digits=20,
                                 blank=True, null=True, default=0)
    date_posted = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return f"Invoice {self.company.supplier_reference} from {self.company.name}"
