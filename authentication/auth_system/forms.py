from django import forms
from .models import Airplane, Flight


class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = "__all__"


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            "airline",
            "flight_number",
            "departure_airport",
            "departure_datetime",
            "arrival_airport",
            "arrival_datetime",
            "base_price",
            "airplane",
            "status",
        ]
        widgets = {
            "departure_datetime": forms.TextInput(attrs={"class": "datepicker"}),
            "arrival_datetime": forms.TextInput(attrs={"class": "datepicker"}),
        }
