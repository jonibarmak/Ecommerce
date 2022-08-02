from django.shortcuts import render
from blog.models import Articles 

def create_article(request):
    new_article=Articles.objects.create(
        title="Bajo el bitcoin",
        description="esta muy bajo",
        author="Mariano Perez")
    context={ 
        "new_article":new_article
    }
    return render(request,"articles/new_article.html",context=context)

def list_products(request):
    products= Products.objects.all()
    context={
        "products":products
    }
    return render(request,"products_list.html",context=context)
