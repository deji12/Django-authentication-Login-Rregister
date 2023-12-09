from django.urls import path
from .views import (
    Customer_HomePage,
    Staff_HomePage,
    Customer_Register,
    Staff_Register,
    Login,
    logoutuser,
    Home,
)

urlpatterns = [
    path("", Home, name="home"),
    path("customer/", Customer_HomePage, name="customer-homepage"),
    path("staff/", Staff_HomePage, name="staff-homepage"),
    path("customer/register/", Customer_Register, name="customer-register"),
    path("staff/register/", Staff_Register, name="staff-register"),
    path("login/", Login, name="login-page"),
    path("logout/", logoutuser, name="logout"),
]
