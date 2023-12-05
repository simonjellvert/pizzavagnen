from datetime import date
from django import forms
from django.forms import DateInput, TimeInput
from .models import Booking


class BookingForm(forms.ModelForm):
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
                'min': min}),
            'booking_time': TimeInput(attrs={
                'class': 'timepicker', 'min': '12:00', 'max': '23:00',
                'type': 'time',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].widget.attrs['min'] = str(date.today())
