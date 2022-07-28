from django.contrib import admin
from django.urls import path
from Ecommerce.views import segundo_template,template_con_lista
from products.views import create_product, list_products 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("segundo_template/",segundo_template,name="segundo_template"),
    path("template_con_lista/",template_con_lista,name="template_con_lista"),
    path("create_product/",create_product,name="create_product"),
    path("list_products/",list_products,name="list_products")

]
