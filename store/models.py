from django.db import models

# Create your models here.
class Address(models.Model):
    addressid = models.BigAutoField(db_column='AddressId', primary_key=True)  # Field name made lowercase.
    own = models.TextField(db_column='Own')  # Field name made lowercase. This field type is a guess.
    addresss = models.CharField(db_column='Addresss', max_length=10000)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=500)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=500)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=500)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'address'
class Customer(models.Model):
    customerid = models.BigAutoField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=500)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.BigIntegerField(db_column='PhoneNumber')  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')  # Field name made lowercase.
    dob = models.DateField(db_column='DoB')  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'customer'
class Category(models.Model):
    categoryid = models.BigAutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'category'
class Manufacturer(models.Model):
    manufacturerid = models.BigAutoField(db_column='ManufacturerId', primary_key=True)  # Field name made lowercase.
    manufacturername = models.CharField(db_column='ManufacturerName', max_length=500)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'manufacturer'
class Product(models.Model):
    productid = models.BigAutoField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=500)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=500)  # Field name made lowercase.
    productdetails = models.CharField(db_column='ProductDetails', max_length=5000)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    manufacturerid = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, db_column='ManufacturerId')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='CategoryId')  # Field name made lowercase.
    otherinfo = models.CharField(db_column='OtherInfo', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'product'
class Binlocation(models.Model):
    binlocationid = models.BigAutoField(db_column='BinLocationId', primary_key=True)  # Field name made lowercase.
    zonenumber = models.BigIntegerField(db_column='ZoneNumber')  # Field name made lowercase.
    areanumber = models.BigIntegerField(db_column='AreaNumber')  # Field name made lowercase.
    binnumber = models.BigIntegerField(db_column='BinNumber')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'binlocation'
class Brand(models.Model):
    brandid = models.BigAutoField(db_column='BrandId', primary_key=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=500)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    categoryid = models.ForeignKey('Category', on_delete=models.CASCADE, db_column='CategoryId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'brand'
class Offer(models.Model):
    offerid = models.BigAutoField(db_column='OfferId', primary_key=True)  # Field name made lowercase.
    offername = models.CharField(db_column='OfferName', max_length=500)  # Field name made lowercase.
    offertype = models.IntegerField(db_column='OfferType')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'offer'
class Buygetfree(models.Model):
    buygetfreeid = models.BigAutoField(db_column='BuyGetFreeId', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    offerid = models.ForeignKey('Offer', on_delete=models.CASCADE, db_column='OfferId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'buygetfree'
class Discount(models.Model):
    discountid = models.BigAutoField(db_column='DiscountId', primary_key=True)  # Field name made lowercase.
    offerid = models.ForeignKey('Offer', on_delete=models.CASCADE, db_column='OfferId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000)  # Field name made lowercase.
    percent = models.FloatField(db_column='Percent')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'discount'
class Ordertocart(models.Model):
    ordertocartid = models.BigAutoField(db_column='OrderToCartId', primary_key=True)  # Field name made lowercase.
    offerid = models.ForeignKey(Offer, on_delete=models.CASCADE, db_column='OfferId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ordertocart'
class Cart(models.Model):
    cartid = models.BigAutoField(db_column='CartId', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    ordertocartid = models.ForeignKey('Ordertocart', on_delete=models.CASCADE, db_column='OrderToCartId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cart'
class Checkout(models.Model):
    checkoutid = models.BigAutoField(db_column='CheckoutId', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    ordertocartid = models.ForeignKey('Ordertocart', on_delete=models.CASCADE, db_column='OrderToCartId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'checkout'
class Checkoutdeliveryid(models.Model):
    checkoutdeliveryid = models.BigAutoField(db_column='CheckoutDeliveryId', primary_key=True)  # Field name made lowercase.
    deliverytype = models.IntegerField(db_column='DeliveryType')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=500)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'checkoutdeliveryid'
class Employee(models.Model):
    employeeid = models.BigAutoField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=500)  # Field name made lowercase.
    gender = models.IntegerField()
    designation = models.CharField(db_column='Designation', max_length=500)  # Field name made lowercase.
    salary = models.FloatField(db_column='Salary')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'employee'
class Deliveraddress(models.Model):
    deliveraddressid = models.BigAutoField(db_column='DeliverAddressId', primary_key=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'deliveraddress'
class Dynamicdelivery(models.Model):
    dynamicdeliveryid = models.BigAutoField(db_column='DynamicDeliveryId', primary_key=True)  # Field name made lowercase.
    deliveraddressid = models.ForeignKey(Deliveraddress, on_delete=models.CASCADE, db_column='DeliverAddressId')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dynamicdelivery'
class Gift(models.Model):
    giftid = models.BigAutoField(db_column='GiftId', primary_key=True)  # Field name made lowercase.
    offerid = models.ForeignKey('Offer', on_delete=models.CASCADE, db_column='OfferId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'gift'
class Inventory(models.Model):
    inventoryid = models.BigAutoField(db_column='InventoryId', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    emptyy = models.TextField(db_column='Emptyy')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'inventory'
class Login(models.Model):
    loginid = models.BigAutoField(db_column='LoginId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500)  # Field name made lowercase.
    passworda = models.CharField(db_column='Passworda', max_length=500)  # Field name made lowercase.
    referralcode = models.CharField(db_column='ReferralCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'login'
class Mutlipleaddress(models.Model):
    multipleaddressid = models.BigAutoField(db_column='MultipleaddressId', primary_key=True)  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    productid = models.ForeignKey('Product', on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    finish = models.TextField(db_column='Finish')  # Field name made lowercase. This field type is a guess.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mutlipleaddress'
class Queries(models.Model):
    queryid = models.BigAutoField(db_column='QueryId', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    dynamicdeliveryid = models.ForeignKey(Dynamicdelivery, on_delete=models.CASCADE, db_column='DynamicDeliveryId')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    queryinfo = models.CharField(db_column='QueryInfo', max_length=500)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'queries'
class Returnss(models.Model):
    returnid = models.BigAutoField(db_column='ReturnId', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    issues = models.CharField(db_column='Issues', max_length=5000)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'returnss'
class Returnit(models.Model):
    returnitid = models.BigAutoField(db_column='ReturnItId', primary_key=True)  # Field name made lowercase.
    returnid = models.ForeignKey('Returnss', on_delete=models.CASCADE, db_column='ReturnId')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'returnit'
class Store(models.Model):
    storeid = models.BigAutoField(db_column='StoreId', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='StoreName', max_length=500)  # Field name made lowercase.
    inchargename = models.CharField(db_column='InchargeName', max_length=500)  # Field name made lowercase.
    phonenumber = models.BigIntegerField(db_column='Phonenumber')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'store'
class Storecollect(models.Model):
    storecollectid = models.BigAutoField(db_column='StoreCollectId', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='StoreId')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkout, on_delete=models.CASCADE, db_column='CheckoutId')  # Field name made lowercase.
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    searchaddress = models.CharField(db_column='SearchAddress', max_length=5000)  # Field name made lowercase.
    finish = models.TextField(db_column='Finish')  # Field name made lowercase. This field type is a guess.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'storecollect'
class Trackdelivery(models.Model):
    trackid = models.BigAutoField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='CustomerId')  # Field name made lowercase.
    dynamicdeliveryid = models.ForeignKey(Dynamicdelivery, on_delete=models.CASCADE, db_column='DynamicDeliveryId')  # Field name made lowercase.
    pstatus = models.CharField(max_length=500)
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'trackdelivery'
class Vendor(models.Model):
    vendorid = models.BigAutoField(db_column='VendorId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=500)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vendor'
class Vendororder(models.Model):
    vendororderid = models.BigAutoField(db_column='VendorOrderId', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    vendorid = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_column='VendorId')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'vendororder'
class Warehouse(models.Model):
    warehouseid = models.BigAutoField(db_column='WarehouseId', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='ProductId')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='AddressId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'warehouse'
class Delivertowarehouse(models.Model):
    delivertowarehouseid = models.BigAutoField(db_column='DeliverToWarehouseId', primary_key=True)  # Field name made lowercase.
    warehouseid = models.ForeignKey('Warehouse', on_delete=models.CASCADE, db_column='WarehouseId')  # Field name made lowercase.
    vendororderid = models.ForeignKey('Vendororder', on_delete=models.CASCADE, db_column='VendorOrderId')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'delivertowarehouse'
class Shipfromwarehouse(models.Model):
    shipid = models.BigAutoField(db_column='ShipId', primary_key=True)  # Field name made lowercase.
    warehouseid = models.ForeignKey('Warehouse', on_delete=models.CASCADE, db_column='WarehouseId')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='EmployeeId')  # Field name made lowercase.
    deliveraddressid = models.ForeignKey(Deliveraddress, on_delete=models.CASCADE, db_column='DeliverAddressId')  # Field name made lowercase.
    binlocationid = models.ForeignKey(Binlocation, on_delete=models.CASCADE, db_column='BinLocationId')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive')  # Field name made lowercase. This field type is a guess.
    moddate = models.DateField(db_column='ModDate')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'shipfromwarehouse'
