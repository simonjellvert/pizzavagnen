from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']
            existing_bookings = Booking.objects.filter(date=new_booking_date)
            if existing_bookings.exists():
                messages.warning(request, 'This date is already booked.')
                return redirect('booking:booking_list')

            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking created successfully.')
            return redirect('booking:booking_list')

        else:
            print(form.errors)
            print(form.cleaned_data)

    else:
        form = BookingForm()

    return render(request, 'booking/new_booking.html', {'form': form})


def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']

            existing_bookings = Booking.objects.filter(
                date=new_booking_date).exclude(pk=booking_id)

            if existing_bookings.exists():

                return redirect('booking:booking_list')

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
        
