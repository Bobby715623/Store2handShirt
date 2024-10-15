from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import *
 
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # ตั้งชื่อเทมเพลตที่ใช้แสดงรายชื่อวง
    context_object_name = 'products'  # ตั้งชื่อที่ใช้ในเทมเพลตสำหรับรายการวง

class BandListView(ListView):
    model = Band
    template_name = 'band_list.html'  # ตั้งชื่อเทมเพลตที่ใช้แสดงรายชื่อวง
    context_object_name = 'bands'  # ตั้งชื่อที่ใช้ในเทมเพลตสำหรับรายการวง


class AddProductView(View):
    def get(self, request):
        form = ProductForm()  # สร้างฟอร์มเปล่า
        return render(request, 'add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)  # สร้างฟอร์มด้วยข้อมูล POST
        if form.is_valid():
            form.save()  # บันทึกข้อมูล
            return redirect('product_list')  # เปลี่ยนไปยังหน้าที่ต้องการหลังเพิ่มสินค้า
        return render(request, 'add_product.html', {'form': form})  # ส่งฟอร์มกลับไปหากไม่ valid


class AddBandView(View):
    def get(self, request):
        form = BandForm()  # สร้างฟอร์มใหม่
        return render(request, 'add_band.html', {'form': form})

    def post(self, request):
        form = BandForm(request.POST)  # สร้างฟอร์มจากข้อมูล POST
        if form.is_valid():
            form.save()  # บันทึกวงลงฐานข้อมูล
            return redirect('band_list')  # เปลี่ยนไปยังหน้าที่ต้องการหลังเพิ่มวง
        return render(request, 'add_band.html', {'form': form})  # ส่งฟอร์มกลับไปหากไม่ valid