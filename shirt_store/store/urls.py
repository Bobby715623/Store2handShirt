from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('register/', MyRegister.as_view(), name='register'), 
    path('login/', MyLogin.as_view(), name='login'), 
    path('main/', MyMain.as_view(), name='mainpage'), 
    path('logout/', MyLogout.as_view(), name='logout'),
    path('addproduct/', MyProduct.as_view(), name='addproduct'), 
    path('address/<int:id>/', MyCustomerAddress.as_view(), name='address'), 
    path('address/', MyAddress.as_view(), name='myaddress'), 
]