from django.urls import path
from app1.views import *

urlpatterns = [
    path('', index,name='index'),
    path('product/', product,name='product'),
    path('service/', service,name='service'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('testimonial/', testimonial,name='testimonial'),
    path('usersignup/', usersignup,name='usersignup'),
    path('userlogin/', userlogin,name='userlogin'),
    path('changepassword/', userchangepass,name='changepass'),
    path('profile/', userprofile,name='profile'),
    path('vendorlogin/', vendorlogin,name='vendorlogin'),
    path('vendorproduct/', vendorproduct,name='vendorproduct'),
    path('logout/',logout,name='logout'),
    path('vendorlogout/',vendorlogout,name='vendorlogout'),
    path('productcat/<int:id>/',productcat,name="productcat"),
    path('singleproduct/<int:id>',singleproduct,name='singleproduct'),
    path('myorder/',order,name='myorder'),
    path('cart/',cart,name='cart'),
    path('addcart/<int:id>',addcart,name="addcart"),
    path('subnocart/<int:id>',subnocart,name="subnocart"),
    path('add_to_cart/<int:id>/',add_to_cart,name="add_to_cart"),
    path('delete_cartitem/<int:id>',delete_cartitem,name='cdelete'),
    path('shiping/',shiping,name='shiping'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('direct_buy/',direct_buy,name="direct_buy"),
    path('MyorderdetaislView/<int:id>',MyorderdetaislView,name="MyorderdetaislView"),
    path('orderSuccessView/',orderSuccessView,name='orderSuccessView'),
    path('search/', search, name='search'),


]