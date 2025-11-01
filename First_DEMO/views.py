from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def shop(request):
    return render(request, 'shop.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def test2(request):
    products = Product.objects.all()  # Query DB
    print(f"DEBUG VIEW: Số sản phẩm query: {products.count()}")  # Print debug
    context = {'products': products}
    return render(request, 'test2.html', context)  # Path template