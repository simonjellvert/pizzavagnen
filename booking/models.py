from django.db import models
from user.models import CustomUser
from django.conf import settings
from django.core.exceptions import ValidationError


class Booking(models.Model):
    number = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Check if there is already a booking on the specified date
        existing_bookings = Booking.objects.filter(date=self.date)
        if existing_bookings.exists():
            raise ValidationError("A booking already exists for this date.")

        # Continue with the save if there are no conflicts
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} | {self.user.last_name} - {self.date} {self.time}"
