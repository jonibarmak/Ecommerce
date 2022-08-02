from django.contrib import admin
from django.urls import path, include
from Ecommerce.views import segundo_template,template_con_lista
from blog.views import create_article

urlpatterns = [
    path('admin/', admin.site.urls),
    path("segundo_template/",segundo_template,name="segundo_template"),
    path("template_con_lista/",template_con_lista,name="template_con_lista"),
    path("products/",include("products.urls")),
    path("articles/",include("blog.urls"))

]
