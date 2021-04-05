from catalog.models import Vendor, Product
from api.Serializer import VendorSerializer, ProductSerializer, ProductListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.views import APIView


class VendorViewList(APIView):

    def get(self, request, format=None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VendorView(APIView):

    def put(self, request, pk, format=None):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            vendor = Vendor.objects.get(pk=pk)
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductViewList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def put(self, request, pk, format=None):
        products = Product.objects.get(pk=pk)
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            products = Product.objects.get(pk=pk)
            products.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        products = Product.objects.get(pk=pk)
        serializer = ProductSerializer(products)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


def token_request(request):
    try:
        new_token = Token.objects.get_or_create(user=request.user)
        return JsonResponse({'token': new_token[0].key}, status=status.HTTP_200_OK)
    except Exception as message:
        return JsonResponse({'messagem': 'You do not have permission.'}, status=status.HTTP_401_UNAUTHORIZED)