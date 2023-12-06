from django.db import models
from datetime import datetime
from user.models import CustomUser
from django.conf import settings
from django.core.exceptions import ValidationError


class Booking(models.Model):
    """
    Booking model
    """
    
    number = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    last_name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def is_past(self):
        now = datetime.now()
        booking_datetime = datetime.combine(self.date, self.time)
        return booking_datetime < now

    def save(self, *args, **kwargs):
        existing_bookings = Booking.objects.filter(date=self.date)
        if existing_bookings.exists():
            raise ValidationError("A booking already exists for this date.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} | {self.last_name} - {self.date} {self.time}"
