from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from .models import *
from django.db.models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
class MyRegister (View):
    def get(self,request):
        form = RegisterForm()
        context = {"form":form}
        return render(request, 'register.html', context)
    def post(sellf,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.password = make_password(form.cleaned_data['password'])
            customer.save()
            group = Group.objects.get(name='customer')
            customer.group.add(group)
            return redirect('login')
        else:
            return render(request, "register.html", {"form": form})
class MyAddress(View):
    def get(self,request):
        customer_id = request.session.get('customer_id', None)
        try:
            cusaddress = CustomerAdress.objects.filter(customer_id=customer_id)
            context = {'cusadd': cusaddress}
        except CustomerAdress.DoesNotExist:
            context = {'error': 'No address found for this customer.'}

        return render(request, 'myaddress.html', context)
class MyCustomerAddress(View):
    def get(self, request, id):
        form = CustomerAddressForm()
        context = {"form": form, "customer_id": id}
        return render(request, 'addaddress.html', context)

    def post(self, request, id):
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer_id_id = id
            address.save()
            return redirect('mainpage')
        else:
            return render(request, 'addaddress.html', {"form": form, "customer_id": id})
class MyProduct (View):
    def get(self,request):
        form = ProductForm()
        context = {"form":form}
        return render(request, 'register.html', context)
    def post(sellf,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            return redirect('mainpage')
        else:
            return render(request, "addproduct.html", {"form": form})
class MyLogin(View):
    def get(self, request):
        form = CustomerLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                customer = Customer.objects.get(username=username)
                if check_password(password, customer.password):
                    login(request, customer)
                    request.session['customer_id'] = customer.id
                    request.session['customer_first_name'] = customer.first_name
                    return redirect('mainpage')
                else:
                    form.add_error(None, "Invalid username or password")
            except Customer.DoesNotExist:
                form.add_error(None, "No userFound")
        return render(request, 'login.html', {'form': form})  
    
class MyLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
class MyMain(View):
    def get(self,request):
        customer_id = request.session.get('customer_id', None)
        return render(request, 'mainpage.html')
            