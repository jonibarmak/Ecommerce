from django.urls import path
from products.views import list_products,create_product, primer_formulario,search_products, delete_product, update_product  

urlpatterns = [
    path("list-products/",list_products,name="list-products"),
    path("create_product/",create_product,name="create_product"),
    path("primer-formulario/",primer_formulario,name="primer-formulario"),
    path("search-products/",search_products,name="search-products"),
    path("delete-product/<int:pk>/",delete_product,name="delete-product"),
    path("update-product/<int:pk>/",update_product,name="update-product"),

    

]