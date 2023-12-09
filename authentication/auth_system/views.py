from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomerProfile, StaffProfile


@login_required
def Customer_HomePage(request):
    return render(request, "customer/home.html", {})


@login_required
def Staff_HomePage(request):
    return render(request, "staff/index.html", {})


def Customer_Register(request):
    if request.method == "POST":
        # Extract user information from the form
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("uname")
        password = request.POST.get("pass")
        building_number = request.POST.get("building_number")
        street = request.POST.get("street")
        city = request.POST.get("city")
        apartment_number = request.POST.get("apartment_number")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")
        passport_number = request.POST.get("passport_number")
        passport_expiration = request.POST.get("passport_expiration")
        passport_country = request.POST.get("passport_country")
        date_of_birth = request.POST.get("date_of_birth")

        # Create a new user

        new_user = User.objects.create_user(
            username=email, email=email, password=password
        )
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()

        # Create a new customer profile associated with the user
        CustomerProfile.objects.create(
            user=new_user,
            building_number=building_number,
            street=street,
            city=city,
            apartment_number=apartment_number,
            state=state,
            zipcode=zipcode,
            passport_number=passport_number,
            passport_expiration=passport_expiration,
            passport_country=passport_country,
            date_of_birth=date_of_birth,
        )

        return redirect("login-page")

    return render(request, "auth_system/register.html", {})


def Staff_Register(request):
    return render(request, "auth_system/staff_register.html", {})


def Login(request):
    if request.method == "POST":
        name = request.POST.get("uname")
        password = request.POST.get("pass")

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, "customerprofile"):
                return redirect("customer-homepage")
            elif hasattr(user, "staffprofile"):
                return redirect("staff-homepage")
            else:
                return HttpResponse("Error, user does not have a valid profile")
        else:
            return HttpResponse("Error, user does not exist")

    return render(request, "auth_system/login.html", {})


def logoutuser(request):
    logout(request)
    return redirect("login-page")
