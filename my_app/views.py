from django.shortcuts import render
from my_app.models import *

def my_funk(request):
    data = {
        
    }
    return render(request, 'index.html', data)


def uz_page(request):
    news = UzbekistanNews.objects.all()
    data = {
       "yangiliklar": news 
    }
    return render(request, 'uznews.html', data)

def gl_page(request):
    data = {
        
    }
    return render(request, 'glnews.html', data)

def sp_page(request):
    data = {
        
    }
    return render(request, 'spnews.html', data)
