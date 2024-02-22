from datetime import date, timedelta
from django import forms
from django.forms import DateInput, TimeInput
from .models import Booking


class BookingForm(forms.ModelForm):
    """ Booking form for the user """

    last_name = forms.CharField(max_length=20, label='Last Name')

    class Meta:
        model = Booking
        min_date = date.today() + timedelta(days=14)
        fields = ['last_name', 'date', 'time', 'location']
        widgets = {
            'date': DateInput(attrs={
                'class': 'datepicker',
                'type': 'date',
                'min': str(min_date)}),
            'time': TimeInput(attrs={
                'class': 'timepicker',
                'min': '12:00',
                'max': '23:00',
                'type': 'time',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = str(
            date.today() + timedelta(days=14))
