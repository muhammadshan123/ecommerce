from django.urls import path
from . import views

urlpatterns=[
    path('costomer_home',views.cust_home),
    path('customer_mycart',views.cust_cart)
]