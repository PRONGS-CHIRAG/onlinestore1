from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Customer,Address,Inventory,Checkout,Cart,Offer,Ordertocart,Buygetfree,Discount,Category,Brand,Manufacturer,Product,Employee,Store,Login
# Create your views here.
def AcceptCustomer(request):
    if request.method == 'POST':
        address=Address()
        address.addresss=request.POST.get('addresss')
        address.city=request.POST.get('city')
        address.state=request.POST.get('state')
        address.country=request.POST.get('country')
        address.pincode=request.POST.get('pincode')
        #address.isactive=1
        address.moddate=datetime.now()
        address.remarks="Fine"
        #address.own="True"
        address.save()
        aid=Address.objects.latest('addressid')
        print(aid)
        #print(type(ac))
        customer=Customer()
        customer.firstname=request.POST.get('firstname')
        customer.lastname=request.POST.get('lastname')
        customer.email=request.POST.get('email')
        customer.phonenumber=request.POST.get('phonenumber')
        customer.gender=request.POST.get('gender')
        customer.dob=request.POST.get('dob')
        customer.maritalstatus=request.POST.get('maritalstatus')
        customer.addressid=aid
        #customer.isactive=1
        customer.moddate=datetime.now()
        customer.remarks="Fine"
        customer.save()
        return render(request,'store/customer.html')
    else:
        return render(request,'store/customer.html')

def AcceptCategory(request):
    if request.method == 'POST':
        category=Category()
        category.categoryname=request.POST.get('categoryname')
        #category.isactive=1
        category.moddate=datetime.now()
        category.remarks="Fine"
        category.save()
        return render(request,'store/category.html')
    else:
        return render(request,'store/category.html')
def AcceptManufacturer(request):
    if request.method == 'POST':
        address=Address()
        address.addresss=request.POST.get('addresss')
        address.city=request.POST.get('city')
        address.state=request.POST.get('state')
        address.country=request.POST.get('country')
        address.pincode=request.POST.get('pincode')
        #address.isactive=1
        address.moddate=datetime.now()
        address.remarks="Fine"
        #address.own="True"
        address.save()
        aid=Address.objects.latest('addressid')
        manufacturer=Manufacturer()
        manufacturer.manufacturername=request.POST.get('manufacturername')
        manufacturer.addressid=aid
        #manufacturer.isactive=1
        manufacturer.moddate=datetime.now()
        manufacturer.remarks="Fine"
        manufacturer.save()
        return render(request,'store/manufacturer.html')
    else:
        return render(request,'store/manufacturer.html')
def AcceptProduct(request):
    if request.method == 'POST':
        product=Product()
        product.productname=request.POST.get('productname')
        product.image=request.POST.get('image')
        product.productdetails=request.POST.get('productdetails')
        product.price=request.POST.get('price')
        product.quantity=request.POST.get('quantity')
        manname=request.POST.get('manufacturername')
        catname=request.POST.get('categoryname')
        a=Manufacturer.objects.filter(manufacturername=manname).first()
        b=Category.objects.filter(categoryname=catname).first()
        product.manufacturerid=a
        product.categoryid=b
        product.otherinfo=request.POST.get('otherinfo')
        #product.isactive=1
        product.moddate=datetime.now()
        product.remarks="Fine"
        product.save()
        inventory=Inventory()
        c=Product.objects.latest('productid')
        inventory.productid=c
        inventory.quantity=request.POST.get('quantity')
        inventory.moddate=datetime.now()
        inventory.remarks="Fine"
        inventory.save()
        return render(request,'store/product.html')
    else:
        return render(request,'store/product.html')
def AcceptEmployee(request):
    if request.method == 'POST':
        address=Address()
        address.addresss=request.POST.get('addresss')
        address.city=request.POST.get('city')
        address.state=request.POST.get('state')
        address.country=request.POST.get('country')
        address.pincode=request.POST.get('pincode')
        #address.isactive=1
        address.moddate=datetime.now()
        address.remarks="Fine"
        #address.own=1
        address.save()
        addressidrecord=Address.objects.latest('addressid')
        employee=Employee()
        employee.employeename=request.POST.get('employeename')
        employee.gender=request.POST.get('gender')
        employee.designation=request.POST.get('designation')
        employee.salary=request.POST.get('salary')
        employee.addressid=addressidrecord
        #employee.isactive=1
        employee.moddate=datetime.now()
        employee.remarks="Fine"
        employee.save()
        return render(request,'store/employee.html')
    else:
        return render(request,'store/employee.html')
def AcceptStore(request):
    if request.method == 'POST':
        address=Address()
        address.addresss=request.POST.get('addresss')
        address.city=request.POST.get('city')
        address.state=request.POST.get('state')
        address.country=request.POST.get('country')
        address.pincode=request.POST.get('pincode')
        #address.isactive=1
        address.moddate=datetime.now()
        address.remarks="Fine"
        #address.own=1
        address.save()
        addressidrecord=Address.objects.latest('addressid')
        store=Store()
        store.storename=request.POST.get('storename')
        store.inchargename=request.POST.get('inchargename')
        store.phonenumber=request.POST.get('phonenumber')
        store.addressid=addressidrecord
        #store.isactive=1
        store.moddate=datetime.now()
        store.remarks="Fine"
        store.save()
        return render(request,'store/store.html')
    else:
        return render(request,'store/store.html')
def AcceptBrand(request):
    if request.method =='POST':
        address=Address()
        address.addresss=request.POST.get('addresss')
        address.city=request.POST.get('city')
        address.state=request.POST.get('state')
        address.country=request.POST.get('country')
        address.pincode=request.POST.get('pincode')
        #address.isactive=1
        address.moddate=datetime.now()
        address.remarks="Fine"
        #address.own=1
        address.save()
        addressidrecord=Address.objects.latest('addressid')
        prodname = request.POST.get('prodname')
        catname = request.POST.get('catname')
        d=Product.objects.get(productname=prodname)
        did=d.productid
        e=Category.objects.get(categoryname=catname)
        eid=e.categoryid
        brand=Brand()
        brand.brandname=request.POST.get('brandname')
        brand.addressid=addressidrecord
        brand.productid=did
        brand.categoryid=eid
        #brand.isactive=1
        brand.moddate=datetime.now()
        brand.remarks="Fine"
        brand.save()
        return render(request,'store/brand.html')
    else:
        return render(request,'store/brand.html')
def AcceptOffer(request):
    if request.method == 'POST':
        prodname=request.POST.get('productname')
        a=Product.objects.get(productname=prodname)
        aid=a.productid
        offer=Offer()
        offer.offername=request.POST.get('offername')
        offer.offertype=request.POST.get('offertype')
        offer.startdate=request.POST.get('startdate')
        offer.enddate=request.POST.get('enddate')
        offer.productid=aid
        #offer.isactive=1
        offer.moddate=datetime.now()
        offer.remarks="Fine"
        offer.save()
        k=Offer.objects.latest('offerid')
        ki=Offer.objects.get(offername=request.POST.get('offername'))
        ktype=ki.offertype
        kid=ki.offerid
        kpid=ki.productid
        ktype=int(ktype)
        kid=int(kid)
        kpid=int(kpid)
        if ktype ==1:
            bg=BuyGetFree()
            bg.offerid=kid
            bg.productid=kpid
            l=request.POST.get('quantity')
            bg.quantity=2*l
            bg.isactive=1
            bg.moddate=datetime.now()
            bg.remarks="Fine"
            bg.save()
        elif ktype == 2:
            discount=Discount()
            discount.offerid=kid
            discount.productid=kpid
            discount.percent=request.POST.get('percent')
            discount.isactive=1
            discount.moddate=datetime.now()
            discount.remarks="Fine"
            discount.save()
        return render(request,'store/offer.html')
    else:
        return render(request,'store/offer.html')
def AcceptLogin(request):
        if request.method =='POST':
            lemail=request.POST.get('email')
            lpass=request.POST.get('password')
            ref=request.POST.get('referralcode')
            a=Customer.objects.get(email=lemail)

            if a != None:
                login=Login()
                login.email=lemail
                login.passworda=lpass
                login.referralcode=ref
                #login.isactive=1
                login.moddate=datetime.now()
                login.remarks="Fine"
                login.customerid=a
                login.save()
            return render(request,'store/acceptlogin.html')
        else:
            return render(request,'store/acceptlogin.html')
def LogIn(request):
    if request.method =='POST':
        lemail=request.POST.get('email')
        lpass=request.POST.get('password')
        a=Login.objects.get(email=lemail,passworda=lpass)
        if a:
            print("valid user")
            #render the store page with all the products
        else:
            print("Invalid user")
            #render the login page
def AddOrder(request):
    if request.method == 'POST':
        cname = request.POST.get('customername')
        pname = request.POST.get('productname')
        a=Product.objects.get(productname=pname)
        aid=a.productid
        b=Offer.objects.get(productid=aid)
        bid=b.offerid
        ordert=Ordertocart()
        ordert.offerid=bid
        ordert.productid=aid
        #ordert.isactive=1
        ordert.moddate=datetime.now()
        ordert.remarks="fine"
        ordert.save()
        tid=b.offertype
        if tid==1:
            e=Buygetfree.objects.get(offerid=bid)
            eid = e.quantity
            f=2*eid
            fa=a.quantity
            fa=f
            fb=a.price
            tprice = fa * fb
        if tid==2:
            h=Discount.objects.get(offerid=bid)
            hid=h.percent
            hf=hid/100
            k=a.price
            l=k*hf
            tprice = k - l
        oc=Ordertocart.objects.get(productid=aid)
        ocid=oc.ordertocartid
        cus=Customer.objects.get(customername=cname)
        cusid=cus.customerid
        cart = Cart()
        cart.ordertocartid=ocid
        cart.customerid=cusid
        #cart.isactive=1
        cart.moddate=datetime.now()
        cart.remarks="Fine"
        cart.save()
def CheckoutCart(request):
    if request.method=='POST':
        cname = request.POST.get('customername')
        c=Customer.objects.get(firstname=cname)
        cid=c.customerid
        d=Cart.objects.get(customerid=cid)
        dor=d.ordertocartid
        cb=Ordertocart.objects.get(ordertocartid=dor)
        cbid=cb.productid
        a=Product.objects.get(productid=cbid)
        aid=a.price
        b=Offer.objects.get(productid=cbid)
        bid=b.offerid
        tid=b.offertype
        if tid==1:
            e=Buygetfree.objects.get(offerid=bid)
            eid = e.quantity
            f=2*eid
            fa=f
            fb=aid
            tprice = fa * fb
            z=f
        if tid==2:
            h=Discount.objects.get(offerid=bid)
            hid=h.percent
            hf=hid/100
            z=1
            k=aid
            l=k*hf
            tprice = k - l
        p=Inventory.objects.get(productid=cbid)
        pq=p.quantity
        pq=pq-z
        pq=int(pq)
        Inventory.objects.get(productid=cbid).update(quantity=pq)
        checkout=Checkout()
        checkout.quantity=z
        checkout.customerid=cid
        checkout.ordertocartid=dor
        #checkout.isactive=1
        checkout.moddate=datetime.now()
        checkout.remarks="Fine"
        checkout.save()
        return HttpResponse("Hi")
#def CheckoutDelivery(request):
