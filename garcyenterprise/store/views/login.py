from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from store.models.store_users import Store_User
from django.views import View


class Login_Customer(View):
    return_url = None

    def get(self, request):
        Login_Customer.return_url = request.GET.get('return_url')
        return render(request, 'login_customer.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login_Customer.return_url:
                    return HttpResponseRedirect(customer.return_url)
                else:
                    customer.return_url = None
                    return redirect('home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print(email, password)
        return render(request, 'login_customer.html', {'error': error_message})

class Login_Store_User(View):
    return_url = None

    def get(self, request):
        Login_Store_User.return_url = request.GET.get('return_url')
        return render(request, 'login_store_user.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        store_user = Store_User.get_store_user_by_email(email)
        error_message = None
        if store_user:
            flag = check_password(password, store_user.password)
            if flag:
                request.session['store_user'] = store_user.id

                if Login_Store_User.return_url:
                    return HttpResponseRedirect(Login_Store_User.return_url)
                else:
                    Login_Store_User.return_url = None
                    return redirect('home')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print(email, password)
        return render(request, 'login_store_user.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('logout')