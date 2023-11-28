from django.db import models
from django.conf import settings
from booking.models import Booking


class StaffArea(models.Model):
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='staff_bookings',
    )
    first_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_fname',
    )
    last_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_lname',
    )
    email = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_email',
    )
    booking_date = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_date',
    )
    booking_time = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_time',
    )

    confirm_booking = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.booking} | {self.last_name}'
