from django.db import models
from django.conf import settings


class Booking(models.Model):
    """
    Booking model
    """
    booking_id = models.IntegerField()
    first_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='booking_fname',
    )
    last_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='booking_lname',
    )
    email = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='booking_email',
    )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_location = models.TextField(max_length=250)
    booking_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.booking_id} | {self.last_name}'
