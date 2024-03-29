from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_groups():
    # Create the 'Staff' group
    staff_group, created = Group.objects.get_or_create(name="Staff")

    # Create the 'Customer' group
    customer_group, created = Group.objects.get_or_create(name="Customer")


class PhoneNumber(models.Model):
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Card(models.Model):
    CARD_TYPES = [
        ("credit", "Credit"),
        ("debit", "Debit"),
    ]

    card_type = models.CharField(max_length=10, choices=CARD_TYPES)
    card_number = models.CharField(max_length=16)
    name_on_card = models.CharField(max_length=128)
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.card_type} - {self.card_number}"


class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    terminals = models.PositiveIntegerField()

    AIRPORT_TYPES = [
        ("domestic", "Domestic"),
        ("international", "International"),
        ("both", "Both"),
    ]
    airport_type = models.CharField(max_length=15, choices=AIRPORT_TYPES)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Airline(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Airplane(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    identification_number = models.CharField(max_length=255, unique=True)
    number_of_seats = models.PositiveIntegerField()
    manufacturing_company = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    manufacturing_date = models.DateField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.airline} - {self.identification_number}"


class MaintenanceProcedure(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.airplane} Maintenance"


class Flight(models.Model):
    STATUS_CHOICES = [
        ("on_time", "On Time"),
        ("delayed", "Delayed"),
    ]

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=255)
    departure_airport = models.ForeignKey(
        Airport, related_name="departures", on_delete=models.CASCADE
    )
    departure_datetime = models.DateTimeField()
    arrival_airport = models.ForeignKey(
        Airport, related_name="arrivals", on_delete=models.CASCADE
    )
    arrival_datetime = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="on_time")

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"


class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    purchase_datetime = models.DateTimeField()
    passenger_first_name = models.CharField(max_length=128)
    passenger_last_name = models.CharField(max_length=128)
    passenger_date_of_birth = models.DateField()
    credit_card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight} Ticket for {self.passenger_first_name} {self.passenger_last_name}"


class Rating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    rating_number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.flight} Rating by {self.customer}"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    emails = models.ManyToManyField(Email)
    phone_numbers = models.ManyToManyField(PhoneNumber)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return f"Staff Profile - {self.user}"


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    building_number = models.IntegerField()
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    apartment_number = models.IntegerField()
    state = models.CharField(max_length=128)
    zipcode = models.IntegerField()
    passport_number = models.CharField(max_length=128)
    passport_expiration = models.DateField()
    passport_country = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return f"Customer Profile - {self.user}"
