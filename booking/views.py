from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from events.models import Post


@login_required
def booking_list(request):
    form = BookingForm()
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'form': form, 'bookings': user_bookings})


def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']

            # Check for conflicts with existing bookings
            existing_bookings = Booking.objects.filter(date=new_booking_date)
            if existing_bookings.exists():
                message = "An event already exists for this date. Please choose a different date."
                messages.warning(request, message)
                return redirect('booking:booking_list')

            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(event_date=new_booking_date)
            if existing_events.exists():
                message = "An event already exists for this date. Please choose a different date."
                messages.warning(request, message)
                return redirect('booking:booking_list')

            booking = form.save(commit=False)
            booking.user = request.user
            booking.last_name = form.cleaned_data['last_name']
            booking.save()
            messages.success(request, 'Booking created successfully.')
            return redirect('booking:booking_list')

        else:
            messages.error(
                request, 'Form submission failed. Please check the form.')
            print(form.errors)
            print(form.cleaned_data)

    else:
        form = BookingForm()

    return render(request, 'booking/new_booking.html', {'form': form})


def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']

            existing_bookings = Booking.objects.filter(
                date=new_booking_date).exclude(pk=pk)

            # Check for conflicts with existing bookings
            if existing_bookings.exists():
                messages.warning(request, 'This date is already booked.')
                return redirect('booking:booking_list')
            
            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(event_date=new_booking_date)
            if existing_events.exists():
                message = "An event already exists for this date. Please choose a different date."
                messages.warning(request, message)
                return redirect('booking:booking_list')

            booking = form.save(commit=False)
            booking.save()
            return redirect('booking:booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/booking_list.html', {'form': form, 'booking': booking})


@login_required
def booking_delete(request, number):
    booking = get_object_or_404(Booking, number=number)
    booking.delete()
    return redirect('booking:booking_list')
