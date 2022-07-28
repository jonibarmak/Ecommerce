from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def segundo_template(request):
    today=datetime.now().date
    context={ 
        "name":"jonathan",
        "lastname":"barmak",
        "today":today
    }
    return render(request,"template_2.html",context=context)

def template_con_lista(request):
    context={ 
        "lista":["tomate","naranja","banana"]
    }
    return render(request,"template_lista.html",context=context)