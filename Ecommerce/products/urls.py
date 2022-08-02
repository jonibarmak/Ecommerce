from django.urls import path
from products.views import list_products,create_product

urlpatterns = [
    path("list-products/",list_products,name="list-products"),
    path("create_product/",create_product,name="create_product"),
    

]