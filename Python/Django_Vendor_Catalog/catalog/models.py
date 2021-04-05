from django.db import models
from django.urls import reverse


class Vendor(models.Model):
    """Model representing a vendor"""

    name = models.CharField(max_length=200, help_text='Enter the name of the vendor')
    cnpj = models.CharField('CNPJ', max_length=14, help_text='Enter only numbers', unique=True)
    city = models.CharField(max_length=50, help_text='Enter the City of the vendor')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendor-detail', args=[str(self.id)])


class Product(models.Model):
    """Model representing a Product"""

    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    product = models.CharField(max_length=50, help_text='Enter the name of the product')
    code = models.CharField(max_length=50, help_text='Enter the code of the product')
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.product

