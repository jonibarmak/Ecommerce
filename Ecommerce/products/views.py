from django.shortcuts import render
from products.models import Products 

def create_product(request):
    new_product=Products.objects.create(name="coca cola 1l",price=350)
    context={ 
        "new_product":new_product
    }
    return render(request,"new_product.html",context=context)

def list_products(request):
    products= Products.objects.all()
    context={
        "products":products
    }
    return render(request,"products_list.html",context=context)
