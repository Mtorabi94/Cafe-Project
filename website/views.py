from django.shortcuts import render
from .models import Category, Product
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request, 'website/index.html')

def menu_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'website/index.html', context)
