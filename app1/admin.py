from django.contrib import admin
from .models import UserRegister,VendorRegister,Product_Category,Product,Contactus,Cartmodel,OrderModel
# Register your models here.

class userregister(admin.ModelAdmin):
    list_display=['username','useremail','usercontactno','usergender','user_DOB',]
admin.site.register(UserRegister,userregister)

class vendorregister(admin.ModelAdmin):
    list_display=['id','vendorname','vendoremail','vendorcontactno','company_address','vendor_GST_no',]
admin.site.register(VendorRegister,vendorregister)

admin.site.register(Product_Category)

class categoryproduct(admin.ModelAdmin):
    list_display=['id','category','productName','productPrice']
admin.site.register(Product,categoryproduct)

class Contactusdisp(admin.ModelAdmin):
    list_display=['name','email','subject']
admin.site.register(Contactus,Contactusdisp)

class CartAdmin(admin.ModelAdmin):
    list_display = ['orderId','userId','productId','quantity','price','totalprice']
admin.site.register(Cartmodel,CartAdmin)

# class OrderModelAdmin(admin.ModelAdmin):
#     list_display = ['orderId','userName','userEmail','orderAmount','orderDate']
admin.site.register(OrderModel)