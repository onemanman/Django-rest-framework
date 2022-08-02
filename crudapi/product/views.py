from django.shortcuts import render
from rest_framework import generics
from .models import Product,Category,Branch,Attribute,DeviceAttribute
from .serializers import ProductSerializer, CategorySerializers, BranchSerializers, AttributeSerializers,DeviceAttributeSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CategoryList(APIView):
    serializer_class = CategorySerializers

    def get(self,request, format = None):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = CategorySerializers

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BranchList(APIView):
    serializer_class = BranchSerializers
    def get(self,request, format = None):
        branch = Branch.objects.all()
        serializer = BranchSerializers(branch, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BranchSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = BranchSerializers

    def get_object(self, pk):
        try:
            return Branch.objects.get(pk=pk)
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializers(branch)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializers(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        branch = self.get_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):
    serializer_class = ProductSerializer

    def get(self,request, format = None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):

    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttributeList(APIView):
    serializer_class = AttributeSerializers

    def get(self, request, format=None):
        attribute = Attribute.objects.all()
        serializer = AttributeSerializers(attribute, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttributeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttributeDetail(APIView):
    serializer_class = AttributeSerializers

    def get_object(self, pk):
        try:
            return DeviceAttribute.objects.get(pk=pk)
        except DeviceAttribute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        attribute = self.get_object(pk)
        serializer = AttributeSerializer(attribute)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        attribute = self.get_object(pk)
        serializer = AttributeSerializer(attribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        attribute = self.get_object(pk)
        attribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeviceAttributeList(APIView):
    serializer_class = DeviceAttributeSerializers

    def get(self, request, format=None):
        device_attribute = DeviceAttribute.objects.all()
        serializer = DeviceAttributeSerializers(device_attribute, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceAttributeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeviceAttributeDetail(APIView):
    serializer_class = DeviceAttributeSerializers

    def get_object(self, pk):
        try:
            return DeviceAttribute.objects.get(pk=pk)
        except DeviceAttribute.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        deviceattribute = self.get_object(pk)
        serializer = DeviceAttributeSerializers(deviceattribute)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        deviceattribute = self.get_object(pk)
        serializer = DeviceAttributeSerializers(deviceattribute, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        deviceattribute = self.get_object(pk)
        deviceattribute.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)