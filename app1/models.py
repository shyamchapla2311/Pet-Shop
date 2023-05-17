from django.db import models

# Create your models here.
class UserRegister(models.Model):
    username=models.CharField(max_length=20,default='',verbose_name='User Name')
    useremail=models.EmailField(max_length=50,verbose_name='Email',default=None)
    usercontactno=models.IntegerField(default='',verbose_name='Contact No')
    g = [
        (None, 'select gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    usergender=models.CharField(max_length=12,choices=g,default=None)
    userimage=models.ImageField(upload_to="user")
    user_DOB=models.DateField(default=None)
    user_address=models.TextField(default=None)
    userpassword=models.CharField(default=None,max_length=20,verbose_name='Password')
    
    def __str__(self):
        return self.username

class VendorRegister(models.Model):
    vendorname=models.CharField(max_length=20,default='',verbose_name='Vendor Name')
    vendoremail=models.EmailField(max_length=50,verbose_name='Email')
    vendorcontactno=models.IntegerField(default='',verbose_name='Contact No')
    company_address=models.TextField()
    vendorimage=models.ImageField(upload_to="Vendor",default=None)
    vendorpassword=models.CharField(max_length=20,verbose_name='Password')
    vendor_GST_no=models.CharField(max_length=50,verbose_name='Vendor GST No')
    
    def __str__(self):
        return self.vendorname

class Product_Category(models.Model):
    name=models.CharField(max_length=20,verbose_name='Category Name')
    img=models.ImageField(upload_to="Category")
    def __str__(self):
        return self.name

class Product(models.Model):
    vendorId=models.CharField(max_length=100)
    category = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField(default=0)
    productDescription = models.TextField(default="")
    productImage = models.ImageField(upload_to="product")

    def __str__(self):
        return self.productName

class Contactus(models.Model):
    name=models.CharField(max_length=20,default='',verbose_name=' Name')
    email=models.EmailField(max_length=50,verbose_name='Email')
    subject=models.CharField(max_length=20,default='',verbose_name=' Subject')
    message=models.TextField()
    
    def __str__(self):
        return self.name

class Cartmodel(models.Model):
    orderId=models.CharField(max_length=200)
    userId=models.CharField(max_length=200)
    productId=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    totalprice=models.CharField(max_length=200)

    def __str__(self):
        return self.orderId

class OrderModel(models.Model):
    userId = models.CharField(max_length=20)
    userName = models.CharField(max_length=100)
    userEmail = models.CharField(max_length=100)
    userContact = models.BigIntegerField()
    address = models.TextField()
    orderAmount = models.CharField(max_length=50)
    paymentVia = models.CharField(max_length=50 ,default="")
    paymentMethod = models.CharField(default=None,max_length=50)
    transactionId = models.TextField(default=None)
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)
    
    def __str__(self) -> str:
        orderId = self.pk
        return str(orderId)