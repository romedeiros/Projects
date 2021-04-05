from django.shortcuts import render
from django.views import generic
from catalog.models import Vendor, Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    """View function for home page"""

    # generate counts of the main objects
    num_vendors = Vendor.objects.all().count()
    num_products = Product.objects.count()

    context = {
        'num_vendors': num_vendors,
        'num_products': num_products
    }

    return render(request, 'index.html', context=context)


class VendorsList(generic.ListView):
    model = Vendor
    paginate_by = 10


class VendorDetail(generic.DetailView):
    model = Vendor


class VendorDelete(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendors')


class VendorCreate(CreateView):
    model = Vendor
    fields = '__all__'


class VendorUpdate(UpdateView):
    model = Vendor
    fields = '__all__'


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('index')


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('index')


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('index')
