from api.views import VendorView, token_request, ProductView, VendorViewList, ProductViewList
from django.urls import path

urlpatterns = [
     path('vendors/<int:pk>', VendorView.as_view(), name='vendor_api'),
     path('vendors', VendorViewList.as_view(), name='vendors_list_api'),
     path('token', token_request, name='token'),
     path('products', ProductViewList.as_view(), name='products_list_api'),
     path('product/<int:pk>', ProductView.as_view(), name='product_api'),
    ]
