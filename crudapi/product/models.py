from django.db import models

# Create your models here.

class Category(models.Model):
    catg_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.catg_name

class Branch(models.Model):
    branch_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.branch_name

class Attribute(models.Model):
    att_name = models.CharField(max_length=100,null=False,blank=False,unique=True)

    def __str__(self):
        return self.att_name


class Product(models.Model):
    name = models.CharField(max_length=100,null=False, blank=True)
    color = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class DeviceAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100,null=False,blank=True)







