from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


@login_required
def booking_list(request):
    form = BookingForm()
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            booking = form.save(commit=False)
            booking.first_name = request.user
            booking.last_name = request.user
            booking.email = request.user
            booking.save()
            return redirect('booking:booking_list')

        else:
            print(form.errors)
            print(form.cleaned_data)

    else:
        form = BookingForm()

    return render(request, 'booking/new_booking.html', {'form': form})


@login_required
def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('booking:booking_list')
        
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'booking/booking_form.html', {'form': form})


@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    booking.delete()
    return redirect('booking:booking_list')
        
