from django.urls import path
from .views import (
    booking_list,
    booking_detail,
    booking_create,
    booking_edit,
    booking_delete,
)


app_name = 'booking'

urlpatterns = [
    path('list/', booking_list, name='booking_list'),
    path('<int:number>/', booking_detail, name='booking_detail'),
    path('create/', booking_create, name='booking_create'),
    path('edit/<int:pk>/', booking_edit, name='booking_edit'),
    path('<int:number>/delete/', booking_delete, name='booking_delete'),
]
