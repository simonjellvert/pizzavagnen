from django.db import models
from django.conf import settings


class Booking(models.Model):
    """
    Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_location = models.TextField(max_length=250)
    booking_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.booking_id:
            last_booking = Booking.objects.order_by('-booking_id').first()
            if last_booking:
                self.booking_id = last_booking.booking_id + 1
            else:
                self.booking_id = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.booking_id} | {self.user.last_name}'
