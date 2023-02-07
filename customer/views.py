from django.shortcuts import render

# Create your views here.
def cust_home(request):
    return render(request,'customer/home.html')
    
def cust_cart(request):
    return render (request,) 'customer/mycart.html'
    