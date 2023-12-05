from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'booking_date',
        'booking_time',
        'booking_location',
        'booking_created'
    )

    list_filter = ('user', 'booking_date')


admin.site.register(Booking, BookingAdmin)
