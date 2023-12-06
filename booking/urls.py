from django.urls import path
from .views import (
    BookingList,
    booking_detail,
    booking_create,
    booking_edit,
    booking_delete,
    staff_booking_list
)


app_name = 'booking'

urlpatterns = [
    path('', BookingList.as_view(), name='booking_list'),
    path('<int:number>/', booking_detail, name='booking_detail'),
    path('create/', booking_create, name='booking_create'),
    path('edit/<int:pk>/', booking_edit, name='booking_edit'),
    path('<int:number>/delete/', booking_delete, name='booking_delete'),
    path('staff/', staff_booking_list, name='staff_booking_list'),
]
