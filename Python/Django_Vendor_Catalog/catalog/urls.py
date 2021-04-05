from catalog import views
from django.urls import path

urlpatterns = [
     path('', views.index, name='index'),
     path('vendors/', views.VendorsList.as_view(), name='vendors'),
     path('vendor/<int:pk>', views.VendorDetail.as_view(), name='vendor-detail'),
     path('vendor/create/', views.VendorCreate.as_view(), name='vendor_create'),
     path('vendor/<int:pk>/update/', views.VendorUpdate.as_view(), name='vendor_update'),
     path('vendor/<int:pk>/delete/', views.VendorDelete.as_view(), name='vendor_delete'),
     path('vendor/new_product/', views.ProductCreate.as_view(), name='product_create'),
     path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
     path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
]