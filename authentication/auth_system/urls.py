from django.urls import path
from .views import (
    Customer_HomePage,
    Staff_HomePage,
    Customer_Register,
    Login,
    logoutuser,
)

urlpatterns = [
    path("customer/", Customer_HomePage, name="customer-homepage"),
    path("staff/", Staff_HomePage, name="staff-homepage"),
    path("customer/register/", Customer_Register, name="customer-register"),
    path("staff/register/", Customer_Register, name="staff-register")
    path("login/", Login, name="login-page"),
    path("logout/", logoutuser, name="logout"),
]
