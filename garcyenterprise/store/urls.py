from django.contrib import admin
from django.urls import path
from .views.home import home, store
from .views.check_inventory import CheckInventory, store_inventory, store_inventory_all
from django.contrib.auth import views as auth_views
from .views.user_category import Signup_User_Category, Login_User_Category
from .views.signup import Signup_Store_User, Signup_Customer
from .views.login import Login_Store_User, Login_Customer, logout
from .middlewares.auth import auth_middleware

#from .middlewares.auth import  auth_middleware

#app_name = "store"
urlpatterns = [
    path('home/', home, name='home'),
    path('home/store/<str:id>', store, name='store'),
    path('home/view_inventory', CheckInventory.as_view(), name='view_inventory'),
    path('home/home/view_inventory/store_inventory', store_inventory_all, name='store_inventory_All'),
    path('home/home/view_inventory/store_inventory/<str:id>', store_inventory, name='store_inventory'),
    path('signup_user_category', Signup_User_Category.signup_check, name='signup_user_category'),
    path('login_user_category', Login_User_Category.login_check, name='login_user_category'),
    path('signup_store_user', Signup_Store_User.as_view(), name='signup_store_user'),
    path('signup_customer', Signup_Customer.as_view(), name='signup_customer'),
    path('login_store_user', Login_Store_User.as_view(), name='login_store_user'),
    path('login_customer', Login_Customer.as_view(), name='login_customer'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),


    ]