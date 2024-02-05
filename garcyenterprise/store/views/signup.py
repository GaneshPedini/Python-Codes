from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.store_users import Store_User
from store.models.customers import Customer
from django.views import View


class Signup_Store_User (View):
    def get(self, request):
        return render(request, 'signup_store_user.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        store_user = Store_User(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateStoreUser(store_user)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            store_user.password = make_password(store_user.password)
            store_user.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup_store_user.html', data)

    def validateStoreUser(self, store_user):
        error_message = None
        if (not store_user.first_name):
            error_message = "Please Enter your First Name !!"
        elif len(store_user.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not store_user.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(store_user.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not store_user.phone:
            error_message = 'Enter your Phone Number'
        elif len(store_user.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(store_user.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(store_user.email) < 5:
            error_message = 'Email must be 5 char long'
        elif store_user.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


class Signup_Customer(View):
    def get(self, request):
        return render(request, 'signup_customer.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup_customer.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len(customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message

