from rest_framework import serializers
from product.models import Product,Category,Branch,Attribute,DeviceAttribute

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','color','category','branch']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','catg_name']


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','branch_name']

class AttributeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'att_name']

class DeviceAttributeSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeviceAttribute
        fields = ['id', 'product', 'attribute', 'value']



