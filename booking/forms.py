from datetime import date
from django.forms import ModelForm, DateInput, TimeInput
from .models import Booking


class NewBookingForm(ModelForm):
    """
    Booking form to the user
    """
    class Meta:
        model = Booking
        min = date.today()
        fields = ['booking_date', 'booking_time', 'booking_location']
        widgets = {
            'booking_date': DateInput(attrs={
                'class': 'datepicker',
                'type': 'date',
                'min': min,
            }),
            'booking_time': TimeInput(attrs={
                'class': 'timepicker',
                'type': 'time',
            })
        }
