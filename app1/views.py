from django.shortcuts import render,redirect
from .form import UserRegisterForm
from .models import UserRegister,VendorRegister,Product_Category,Product,Contactus,Cartmodel,OrderModel
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.db.models import Q
# Create your views here.


def index(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        category=Product_Category.objects.all()
        
        return render (request,'index.html',{'sessionuser':user,'name':data,'category':category})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        category=Product_Category.objects.all()       
        return render (request,'index.html',{'sessionvendor':vendor,'name':data,'category':category})
    else:
        category=Product_Category.objects.all()
        return render (request,'index.html',{'category':category})
    
def product(request):
    if request.session.has_key('AddCartMessage'):
        message = request.session['AddCartMessage']
        del request.session['AddCartMessage']
    else:
        message = ''

    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        category=Product_Category.objects.all()
        productdata=Product.objects.all()
        return render (request,'product.html',{'sessionuser':user,'name':data,'category':category,'productdata':productdata,'m':message})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        category=Product_Category.objects.all()
        data=VendorRegister.objects.get(vendoremail=vendor)
        productdata=Product.objects.filter(vendorId=request.session['vendorId'])
        return render (request,'product.html',{'sessionvendor':vendor,'name':data,'category':category,'productdata':productdata,'m':message})
    else:
        category=Product_Category.objects.all()
        productdata=Product.objects.all()
        return render (request,'product.html',{'category':category,'productdata':productdata,'m':message})   

def productcat(request,id):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        category=Product_Category.objects.all()
        # print(category)
        
        productdata=Product.objects.filter(category=id)
        print(category)
        return render (request,'product.html',{'sessionuser':user,'name':data,'category':category,'productdata':productdata})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        category=Product_Category.objects.all()
        data=VendorRegister.objects.get(vendoremail=vendor)
        productdata=Product.objects.filter(vendorId=request.session['vendorId']) & Product.objects.filter(category=id)
        return render (request,'product.html',{'sessionvendor':vendor,'name':data,'category':category,'productdata':productdata})
    else:
        category=Product_Category.objects.all()
        productdata=Product.objects.filter(category=id)
        return render (request,'product.html',{'category':category,'productdata':productdata})
def service(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'service.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'service.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'service.html')
def search(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        query = request.GET.get('search')
        qset = query.split(' ')
        print(qset)
        for q in qset:
            b = Product.objects.filter(Q(category__name__icontains=q) | Q(
                productName__icontains=q) | Q(productPrice__icontains=q)).distinct()
        return render(request, 'search.html', {'sessionuser':user,'name':data,'productdata': b})
    else:
        return redirect('userlogin')


def about(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'about.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'about.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'about.html')

def contact(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.subject=request.POST['subject']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'sessionuser':user,'name':data,'messagekey':'message sent'})
        return render (request,'contact.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.subject=request.POST['subject']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'sessionvendor':vendor,'name':data,'messagekey':'message sent'})
        return render (request,'contact.html',{'sessionvendor':vendor,'name':data})
    else:
        if request.method=="POST":
            model=Contactus()
            model.name=request.POST['name']
            model.email=request.POST['email']
            model.subject=request.POST['subject']
            model.message=request.POST['message']
            model.save()
            return render (request,'contact.html',{'messagekey':'message sent'})
        return render (request,'contact.html')

def testimonial(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render (request,'testimonial.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        return render (request,'testimonial.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'testimonial.html')

def usersignup(request):
    obj=UserRegisterForm(request.POST,request.FILES) 
    print(obj)
    if obj.is_valid():
        data=UserRegister.objects.all().filter(useremail=request.POST['useremail'])
        if len(data)<=0:
            obj.save()
            return redirect('userlogin')
        else:
            return render(request,'usersignup.html',{'messagekey':"User Already Exists"})
    return render(request,'usersignup.html')

def userlogin(request):
    if request.POST:
        email = request.POST['useremail']
        pass1 = request.POST['userpassword']
        try:
            valid = UserRegister.objects.get(useremail=email,userpassword=pass1)
            if valid:
                request.session['user'] = email
                request.session['username'] = valid.username
                request.session['usercontactno'] = valid.usercontactno
                request.session['user_address'] = valid.user_address
                request.session['userId'] = valid.pk
                return redirect('index')
            else:
                return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'userlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'userlogin.html')

def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('userlogin')
    return redirect('userlogin')

def userchangepass(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        if request.method=="POST":
            if data.userpassword==request.POST['old'] :
                if request.POST['new']==request.POST['c_new']:
                    data.userpassword=request.POST['new']
                    data.save()
                    return render (request,'userchangepass.html',{'sessionuser':user,'name':data,'m':"Password Save"})
                else:
                    return render (request,'userchangepass.html',{'sessionuser':user,'name':data,'m':"new password and conferm password must be same"})
            else:
                return render (request,'userchangepass.html',{'sessionuser':user,'name':data,'m':"type valid old password"})
        return render (request,'userchangepass.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        if request.method=="POST":
            if data.vendorname==request.POST['old'] :
                if request.POST['new']==request.POST['c_new']:
                    data.vendorpassword=request.POST['new']
                    data.save()
                    return redirect('changepass')
                else:
                    return render (request,'userchangepass.html',{'sessionuser':user,'name':data,'m':"new password and conferm password must be same"})
            else:
                return render (request,'userchangepass.html',{'sessionuser':user,'name':data,'m':"type valid old password"})
        return render (request,'userchangepass.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'userchangepass.html')

def userprofile(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        if request.method=='POST':
            data.username=request.POST['name']
            data.usercontactno=request.POST['number']
            data.user_address=request.POST['address']
            data.save()
            return redirect('profile')
        return render (request,'userprofile.html',{'sessionuser':user,'name':data})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        if request.method=='POST':
            data.vendorname=request.POST['name']
            data.vendorcontactno=request.POST['number']
            data.company_address=request.POST['address']
            data.save()
            return redirect('profile')
        return render (request,'userprofile.html',{'sessionvendor':vendor,'name':data})
    else:
        return render (request,'userprofile.html')

def vendorlogin(request):
    if request.POST:
        email = request.POST['vendoremail']
        pass1 = request.POST['vendorpassword']
        try:
            valid = VendorRegister.objects.get(vendoremail=email,vendorpassword=pass1)
            if valid:
                request.session['vendor'] = email
                request.session['vendorId'] = valid.pk
                return redirect('index')
            else:
                return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
        except:
            return render(request,'vendorlogin.html',{'messagekey':'Password incorrect'})
    return render(request,'vendorlogin.html')
def vendorlogout(request):
    if 'vendor' in request.session.keys():
        del request.session['vendor']
        return redirect('vendorlogin')
    return redirect('vendorlogin')
def vendorproduct(request):
    if 'vendor' in request.session.keys():
        vendor= request.session['vendor']
        data=Product_Category.objects.all()
        if request.method=="POST" and request.FILES['image']:
            vendor_id=request.session['vendorId']
            category=Product_Category.objects.get(id=request.POST['product_category'])
            name = request.POST['productname']
            price=request.POST['productPrice']
            discription=request.POST['discription']
            img=request.FILES['image']
            Product.objects.create(vendorId=vendor_id,category=category,productName=name,productPrice=price,productDescription=discription,productImage=img)
        return render(request,'vendorproduct.html',{'sessionvendor':vendor,'ab':data})
    else:
        return redirect('vendorlogin')

def singleproduct(request,id):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        product=Product.objects.get(pk=id)
        b=Cartmodel.objects.filter(productId=product.id)&Cartmodel.objects.filter(orderId="0")
        if request.POST:
            if len(b)<=0:
                model=Cartmodel()
                model.orderId="0"
                model.userId=request.session['userId']
                model.productId=id
                model.quantity="1"
                model.price=product.productPrice
                model.totalprice=str(int(model.quantity)*product.productPrice)
                model.save()
                #return redirect('cart')
                return render(request,'singleproduct.html',{'sessionuser':user,'name':data,'product':product,'m':'Product Added In Cart Successfully'})
            else:
                return render(request,'singleproduct.html',{'sessionuser':user,'name':data,'product':product,'m':'alredy in cart'})
        
        return render (request,'singleproduct.html',{'sessionuser':user,'name':data,'product':product})
    else:
        return redirect(userlogin)



# show add product in cart below demo code
def add_to_cart(request,id):
    if 'user' in request.session:
        a=Product.objects.get(id=id)
        b=Cartmodel.objects.filter(productId=a.id)&Cartmodel.objects.filter(orderId="0")
        print(b)
        if len(b)<=0:
            model=Cartmodel()
            model.orderId="0"
            model.userId=request.session['userId']
            model.productId=id
            model.quantity="1"
            model.price=a.productPrice
            model.totalprice=str(int(model.quantity)*a.productPrice)
            model.save()   
            request.session['AddCartMessage'] = "Product Added In Cart"
            return redirect('product')
            # return render(request,'product.html',{'sessionuser':user,'name':data,'m':'Product Sucessfully added','productdata':c})
        else:
            request.session['AddCartMessage'] = "Product Already Added In Cart"
            return redirect('product')
            
    else:
        return redirect('userlogin')

def cart(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        cartdata=Cartmodel.objects.filter(userId=request.session['userId']) & Cartmodel.objects.filter(orderId="0")
        totalamt=0
        cartlist=[]
        for i in cartdata:
            pk_id=i.pk
            totalamt+=int(i.totalprice)
            producttotalprice=i.totalprice
            productdata=Product.objects.get(pk=i.productId)
            productcat=productdata.category
            productimage=productdata.productImage
            productname=productdata.productName
            productquantity=i.quantity
            productprice=productdata.productPrice
            cartdict={'id':pk_id,'productquantity':productquantity,'productimage':productimage,'productname':productname,'productprice':productprice,'producttotalprice':producttotalprice,'productdis':productcat}
            cartlist.append(cartdict)        
        return render(request,'cart.html',{'sessionuser':user,'name':data,'cart':cartdata,'noitem':len(cartlist),'cartlist':cartlist,'totalamt':totalamt,})
    else:
        return redirect('userlogin')

def addcart(request,id):
    if 'user' in request.session:
        a=Cartmodel.objects.filter(id=id)
        for i in a:
            if int(i.quantity)>0:
                i.quantity=str(int(i.quantity)+1)
                i.totalprice=int(i.price)*int(i.quantity)
                i.save()        
        return redirect('cart')
    else:
        return redirect('userlogin')
def subnocart(request,id):
    if 'user' in request.session:
        a=Cartmodel.objects.filter(id=id)
        for i in a:
            if int(i.quantity)>0:
                i.quantity=str(int(i.quantity)-1)
                i.totalprice=int(i.price)*int(i.quantity)
                i.save()
            else:
                a.delete()        
        return redirect('cart')
    else:
        return redirect('userlogin')


def delete_cartitem(request,id):
    if 'user' in request.session:
        a=Cartmodel.objects.filter(id=id)
        a.delete()
        return redirect('cart')
    else:
        return redirect('userlogin')

def shiping(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        cartdata=Cartmodel.objects.filter(userId=request.session['userId']) & Cartmodel.objects.filter(orderId="0")
        totalamt=0
        cartlist=[]
        for i in cartdata:
            pk_id=i.pk
            totalamt+=int(i.totalprice)
            producttotalprice=i.totalprice
            productdata=Product.objects.get(pk=i.productId)
            productcat=productdata.category
            productimage=productdata.productImage
            productname=productdata.productName
            productquantity=i.quantity
            productprice=productdata.productPrice
            cartdict={'id':pk_id,'productquantity':productquantity,'productimage':productimage,'productname':productname,'productprice':productprice,'producttotalprice':producttotalprice,'productdis':productcat}
            cartlist.append(cartdict) 
        sessionId=request.session['userId']        
        razorpay_amount=totalamt*100
        request.session['shippingUserId'] = sessionId
        request.session['shippingName'] = request.session['username']
        request.session['shippingEmail'] = request.session['user']
        request.session['shippingContact'] = request.session['usercontactno']
        request.session['shippingAddress'] = request.session['user_address']
        request.session['shippingOrderAmount'] = str(totalamt)
        request.session['shippingPaymentVia'] = "Online"
        request.session['shippingPaymentMethod'] = "Razorpay"
        request.session['shippingTransactionId'] = ""
        return redirect('razorpayView')                   
    else:
        return redirect('userlogin')


def order(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        order=OrderModel.objects.filter(userId=request.session['userId'])
        return render (request,'myorder.html',{'sessionuser':user,'name':data,'order':order})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        # data1=Cartmodel.objects.filter(orderId != 0)
        order=OrderModel.objects.all()
        # for i in data1:
        #     pr=Product.objects.filter(vendorId=request.session['vendorId']) and Product.objects.filter(id=i.productId)
        #     print(pr)
        #     # d={
        #     #     'productname':pr.productName
        #     # }
        return render (request,'myorder.html',{'sessionvendor':vendor,'name':data,'order':order})
    else:
        return redirect(userlogin)



RAZOR_KEY_ID = 'rzp_test_8iwTTjUECLclBG'
RAZOR_KEY_SECRET = '0q8iXqBL1vonQGVQn4hK1tYg'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['shippingOrderAmount'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['shippingOrderAmount'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = OrderModel()
            orderModel.userId = request.session['shippingUserId']
            orderModel.userName = request.session['shippingName']
            orderModel.userEmail = request.session['shippingEmail']
            orderModel.userContact = request.session['shippingContact']
            orderModel.address = request.session['shippingAddress']
            orderModel.orderAmount = request.session['shippingOrderAmount']
            orderModel.paymentVia = request.session['shippingPaymentVia']
            orderModel.paymentMethod = request.session['shippingPaymentMethod']
            orderModel.transactionId = payment_id
            orderModel.save()
            orderId = OrderModel.objects.latest('id')
        
            cartdata=Cartmodel.objects.filter(userId=request.session['userId']) & Cartmodel.objects.filter(orderId="0")
            for i in cartdata:
                cartData = Cartmodel.objects.get(id=i.pk)
                cartData.orderId = str(orderId)
                cartData.save()
            # render success page on successful caputre of payment
            return redirect('orderSuccessView')
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()

def direct_buy(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        if request.method=="POST":
            id=request.POST['id']
            product=Product.objects.get(id=id)
            model=Cartmodel()
            model.orderId="0"
            model.userId=request.session['userId']
            model.productId=id
            model.quantity="1"
            model.price=product.productPrice
            model.totalprice=str(int(model.quantity)*product.productPrice)
            model.save()      
            sessionId=request.session['userId']        
            request.session['shippingUserId'] = sessionId
            request.session['shippingName'] = request.session['username']
            request.session['shippingEmail'] = request.session['user']
            request.session['shippingContact'] = request.session['usercontactno']
            request.session['shippingAddress'] = request.session['user_address']
            request.session['shippingOrderAmount'] = str(product.productPrice)
            request.session['shippingPaymentVia'] = "Online"
            request.session['shippingPaymentMethod'] = "Razorpay"
            request.session['shippingTransactionId'] = ""
            return redirect('razorpayView')                   
        
    else:
        return redirect('userlogin')


def MyorderdetaislView(request,id):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        orderData = OrderModel.objects.get(id=id)

        cartQuery = Cartmodel.objects.filter(orderId=id)
        cartDataArray = []
        for i in cartQuery:
            productNameQuery = Product.objects.get(id=i.productId)
            cartDict = {
                'productId':i.productId,
                'productName':productNameQuery.productName,
                'productImage':productNameQuery.productImage.url,
                'productdisc':productNameQuery.productDescription,
                'qty':i.quantity,
                'price':i.price,
                'totalPrice':i.totalprice,
                'orderId':i.orderId
                }
            cartDataArray.append(cartDict)
        return render(request,'orderdetails.html',{'sessionuser':user,'name':data,'CartData':cartDataArray,'orderData':orderData})
    elif request.session.has_key('vendor'):
        vendor= request.session['vendor']
        data=VendorRegister.objects.get(vendoremail=vendor)
        orderData = OrderModel.objects.get(id=id)
        cartQuery = Cartmodel.objects.filter(orderId=id)
        cartDataArray = []
        for i in cartQuery:
            productNameQuery = Product.objects.get(id=i.productId)
            cartDict = {
                'productId':i.productId,
                'productName':productNameQuery.productName,
                'productImage':productNameQuery.productImage.url,
                'productdisc':productNameQuery.productDescription,
                'qty':i.quantity,
                'price':i.price,
                'totalPrice':i.totalprice,
                'orderId':i.orderId
                }
            cartDataArray.append(cartDict)
        return render (request,'orderdetails.html',{'sessionvendor':vendor,'name':data,'CartData':cartDataArray,'orderData':orderData})
    else:
        return redirect('userlogin')


def orderSuccessView(request):
    if request.session.has_key('user'):       
        user= request.session['user']
        data=UserRegister.objects.get(useremail=user)
        return render(request,'order_sucess.html',{'sessionuser':user,'name':data,})
    else:
        return redirect('userlogin')