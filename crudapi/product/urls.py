
from django.urls import path
from .views import *
# from product.views import
# ProductList,ProductDetail

urlpatterns = [
    path('list_category/', CategoryList.as_view()),
    path('list_category/<int:pk>',CategoryDetail.as_view()),
    path('list_branch/',BranchList.as_view()),
    path('list_branch/<int:pk>',BranchDetail.as_view()),
    path('list_product/', ProductList.as_view()),
    path('list_product/<int:pk>',ProductDetail.as_view()),
    path('list_attribute',AttributeList.as_view()),
    path('list_attribute/<int:pk>',AttributeDetail.as_view()),
    path('list_deviceattribute/',DeviceAttributeList.as_view()),
    path('list_deviceattribute/<int:pk>',DeviceAttributeDetail.as_view())
]

