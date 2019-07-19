from django.urls import path

from . import views

urlpatterns=[
path('entercustomer',views.AcceptCustomer,name='acceptcustomer'),
path('enterbrand',views.AcceptBrand,name='acceptbrand'),
path('entermanufacturer',views.AcceptManufacturer,name='acceptmanufacturer'),
path('entercategory',views.AcceptCategory,name='acceptcategory'),
path('enterproduct',views.AcceptProduct,name='acceptproduct'),
path('enteroffer',views.AcceptOffer,name='acceptoffer'),
path('enteremployee',views.AcceptEmployee,name='acceptemployee'),
path('acceptlogin',views.AcceptLogin,name='acceptlogin'),
path('checkout',views.CheckoutCart,name='checkout'),
path('enterstore',views.AcceptStore,name='acceptstore'),
path('acceptlogin',views.AcceptLogin,name='acceptlogin')
]
