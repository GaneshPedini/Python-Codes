from django.shortcuts import render, redirect
from django.views import View

class Signup_User_Category(View):
    def signup_check(request):
        return render(request, 'signup_user_category.html')


class Login_User_Category(View):
    def login_check(request):
        return render(request, 'login_user_category.html')
