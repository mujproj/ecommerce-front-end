from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from loginsystem.models import *
from math import ceil
from .forms import *

keyvalue = 0
session = ''
# Create your views here.

def main(request):
    global session
    keyvalue = 1
    param = {'keyvalue': keyvalue, 'session': session}
    return render(request, 'shopsme/main.html', param)

def index(request):
    if 'username' in request.session:
        username = request.session["username"]
    
    else:
        username = ""
    
    allProds = []
    products = product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    allProds.append([products, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'product': products, 'username': username}
    return render(request, 'shopsme/index.html', params)

def about(request):
    return render(request, 'shopsme/about.html', {})

def contact(request):
    return render(request, 'shopsme/contact.html', {})

def search(request):
    return HttpResponse("Search")

def productview(request):
    a = product.objects.get(product_name = "Laptop")
    print(a.category)
    return render(request, 'shopsme/index.html', {'a': a})

def tracker(request):
    products = product.objects.all()
    param = {'products': products}
    return render(request, 'shopsme/myorder.html', param)

def checkout(request):
    return HttpResponse("checkout")

def accounts(request):
    username = request.session['username']
    email = request.session['emailID']
    # emailId = user.emailID
    param = {'username': username, 'emailID': email}
    return render(request, 'shopsme/dropdown/accounts.html', param)

def help(request):
    return render(request, 'shopsme/dropdown/help.html')

def purchaseperuser(request):
    return render(request, 'shopsme/purchaseperuser.html', {'purchaseuser': purchaseuser})