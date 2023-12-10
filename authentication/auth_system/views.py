from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomerProfile, StaffProfile, Airplane, Flight, Airline
from django.contrib import messages
from .forms import AirplaneForm, FlightForm


@login_required
def Customer_HomePage(request):
    return render(request, "customer/home.html", {})


@login_required
def Staff_HomePage(request):
    user_airline = (
        request.user.staffprofile.airline
    )  # Assuming your StaffProfile model has a 'airline' field

    airplanes = Airplane.objects.filter(airline=user_airline)
    flights = Flight.objects.all()

    if request.method == "POST":
        if "create_airplane" in request.POST:
            airplane_form = AirplaneForm(request.POST)
            if airplane_form.is_valid():
                airplane_form.save()
                return redirect("staff-homepage")
        elif "create_flight" in request.POST:
            flight_form = FlightForm(request.POST)
            flight_form.fields[
                "airplane"
            ].queryset = airplanes  # Limit choices to airplanes of the user's airline
            if flight_form.is_valid():
                flight = flight_form.save(commit=False)
                flight.airline = user_airline
                flight.save()
                return redirect("staff-homepage")
        elif "update_flight_status" in request.POST:
            flight_id = request.POST.get("flight_id")
            new_status = request.POST.get("new_status")
            flight = Flight.objects.get(pk=flight_id)
            flight.status = new_status
            flight.save()
            return redirect("staff-homepage")
    else:
        airplane_form = AirplaneForm()
        flight_form = FlightForm()
        flight_form.fields[
            "airplane"
        ].queryset = airplanes  # Limit choices to airplanes of the user's airline

    return render(
        request,
        "staff/home.html",
        {
            "airplanes": airplanes,
            "flights": flights,
            "airplane_form": airplane_form,
            "flight_form": flight_form,
        },
    )


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
    if request.method == "POST":
        # Extract user information from the form
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        date_of_birth = request.POST.get("date_of_birth")
        airline_name = request.POST.get(
            "airline"
        )  # Adjust this based on your form structure

        # Create a new user
        new_user = User.objects.create_user(username=username, password=password)

        # Add the user to the 'Staff' group
        staff_group = Group.objects.get(name="Staff")
        staff_group.user_set.add(new_user)

        # Create a new staff profile associated with the user and the specified airline
        airline = Airline.objects.get(name=airline_name)  # Retrieve Airline by name
        staff_profile = StaffProfile.objects.create(
            user=new_user,
            date_of_birth=date_of_birth,
            airline=airline,
        )

        return redirect("login-page")

    # Render the registration form
    airlines = (
        Airline.objects.all()
    )  # You may need to adjust this based on your data model
    return render(request, "auth_system/staff_register.html", {"airlines": airlines})


def Login(request):
    if request.method == "POST":
        name = request.POST.get("uname")
        password = request.POST.get("pass")
        user_type = request.POST.get("user_type")

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            if user_type == "customer" and user.groups.filter(name="Customer").exists():
                return redirect("customer-homepage")
            elif user_type == "staff" and user.groups.filter(name="Staff").exists():
                return redirect("staff-homepage")
            else:
                return HttpResponse(
                    "Error, user does not have a valid profile or group"
                )
        else:
            messages.error(request, "Invalid login credentials. Please try again.")

    return render(request, "auth_system/login.html", {})


def logoutuser(request):
    logout(request)
    return redirect("login-page")


def Home(request):
    return render(request, "index.html", {})
