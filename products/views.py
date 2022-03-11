from django.shortcuts import render
from .models import Category,Product
from .services import get_product,get_category
# Create your views here.
def index(request):
    categorys = get_category()
    products = get_product()
    print(products)
    ctx= {
       'categorys' : categorys,
        'products' : products
    }
    return render(request,'index.html',ctx)
def product_view(request):
    categorys = get_category()
    products = get_product()
    ctx = {
        'categorys': categorys,
        'products': products
    }
    return render(request,'product.html',ctx)
    
