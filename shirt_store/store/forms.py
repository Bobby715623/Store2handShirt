
from django import forms
from .models import *
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
PROVINCES = (
    ('กรุงเทพมหานคร', 'กรุงเทพมหานคร'),
    ('กระบี่', 'กระบี่'),
    ('กาญจนบุรี', 'กาญจนบุรี'),
    ('กาฬสินธุ์', 'กาฬสินธุ์'),
    ('กำแพงเพชร', 'กำแพงเพชร'),
    ('ขอนแก่น', 'ขอนแก่น'),
    ('จันทบุรี', 'จันทบุรี'),
    ('ฉะเชิงเทรา', 'ฉะเชิงเทรา'),
    ('ชลบุรี', 'ชลบุรี'),
    ('ชัยนาท', 'ชัยนาท'),
    ('ชัยภูมิ', 'ชัยภูมิ'),
    ('ชุมพร', 'ชุมพร'),
    ('ตรัง', 'ตรัง'),
    ('ตราด', 'ตราด'),
    ('นครนายก', 'นครนายก'),
    ('นครปฐม', 'นครปฐม'),
    ('นครพนม', 'นครพนม'),
    ('นครราชสีมา', 'นครราชสีมา'),
    ('นครศรีธรรมราช', 'นครศรีธรรมราช'),
    ('นนทบุรี', 'นนทบุรี'),
    ('นราธิวาส', 'นราธิวาส'),
    ('น่าน', 'น่าน'),
    ('บุรีรัมย์', 'บุรีรัมย์'),
    ('ปทุมธานี', 'ปทุมธานี'),
    ('ประจวบคีรีขันธ์', 'ประจวบคีรีขันธ์'),
    ('ปราจีนบุรี', 'ปราจีนบุรี'),
    ('ปัตตานี', 'ปัตตานี'),
    ('พะเยา', 'พะเยา'),
    ('พระนครศรีอยุธยา', 'พระนครศรีอยุธยา'),
    ('พังงา', 'พังงา'),
    ('พิจิตร', 'พิจิตร'),
    ('พิษณุโลก', 'พิษณุโลก'),
    ('เพชรบุรี', 'เพชรบุรี'),
    ('เพชรบูรณ์', 'เพชรบูรณ์'),
    ('แพร่', 'แพร่'),
    ('ยโสธร', 'ยโสธร'),
    ('ระนอง', 'ระนอง'),
    ('ระยอง', 'ระยอง'),
    ('ราชบุรี', 'ราชบุรี'),
    ('ลพบุรี', 'ลพบุรี'),
    ('ลำปาง', 'ลำปาง'),
    ('ลำพูน', 'ลำพูน'),
    ('ศรีสะเกษ', 'ศรีสะเกษ'),
    ('สกลนคร', 'สกลนคร'),
    ('สงขลา', 'สงขลา'),
    ('สมุทรปราการ', 'สมุทรปราการ'),
    ('สมุทรสงคราม', 'สมุทรสงคราม'),
    ('สมุทรสาคร', 'สมุทรสาคร'),
    ('สระบุรี', 'สระบุรี'),
    ('สระแก้ว', 'สระแก้ว'),
    ('สุพรรณบุรี', 'สุพรรณบุรี'),
    ('สุราษฎร์ธานี', 'สุราษฎร์ธานี'),
    ('สุรินทร์', 'สุรินทร์'),
    ('อ่างทอง', 'อ่างทอง'),
    ('อุดรธานี', 'อุดรธานี'),
    ('อุทัยธานี', 'อุทัยธานี'),
    ('อุบลราชธานี', 'อุบลราชธานี'),
)
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )
    class Meta:
        model = Customer
        fields = [
            "username",
            "password",
            "password2",
            "first_name", 
            "last_name", 
            "phone", 
            "email", 
            "birthday", 
        ]
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError("Password ไม่ตรงกัน")
        else:
            return cleaned_data
class CustomerLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "image",
            "size",
            "price", 
            "amount", 
            "description", 
            "band_id", 
        ]
class CustomerAddressForm(forms.ModelForm):
    province = forms.ChoiceField(choices=PROVINCES)
    class Meta:
        model = CustomerAdress
        fields = ['province', 'district', 'subdistrict', 'post_num', 'addressinfo']
class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['name', 'code', 'type', 'discount', 'amount', 'expire_date']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'image', 'about', 'category_band']
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_id', 'total_price', 'paymentmethod', 'orderstatus', 'couponid', 'orderproduct']
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product_id', 'customer_id', 'amount', 'price']