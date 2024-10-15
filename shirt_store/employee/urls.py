from django.urls import path

from .views import *

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('band_list/', BandListView.as_view(), name='band_list'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('add_band/', AddBandView.as_view(), name='add_band'),
]