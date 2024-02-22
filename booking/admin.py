from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """ Display and filter bookings in admin panel """
    list_display = (
        'number',
        'get_user_last_name',
        'date',
        'time',
        'location',
        'date_created'
    )

    list_filter = ('user', 'date')

    def get_user_last_name(self, obj):
        return obj.user.last_name


admin.site.register(Booking, BookingAdmin)
