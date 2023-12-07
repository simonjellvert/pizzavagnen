from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
from .models import Booking
from .forms import BookingForm
from events.models import Post


@method_decorator(login_required, name='dispatch')
class BookingList(generic.ListView):
    """
    View for displaying bookings
    """
    model = Booking
    template_name = 'booking/booking_list.html'
    paginate_by = 2

    def get_queryset(self):
        now = datetime.now()
        return Booking.objects.filter(user=self.request.user).order_by('date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm()
        context['bookings'] = self.get_queryset()

        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['bookings'] = paginator.page(page)
        except Exception as e:
            context['bookings'] = paginator.page(1)

        return context


def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})


@login_required
def booking_create(request):
    """
    View for create a new booking
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']

            # Check if the selected date is in the past
            if new_booking_date < timezone.now().date():
                messages.error(
                    request,
                    "You cannot create a booking in the past."
                    "Please choose a future date."
                    )
                return redirect('booking:booking_list')

            # Check for conflicts with existing bookings
            existing_bookings = Booking.objects.filter(date=new_booking_date)
            if existing_bookings.exists():
                messages.error(
                    request,
                    "An event already exists for this date."
                    "Please choose a different date."
                )
                return redirect('booking:booking_list')

            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(event_date=new_booking_date)
            if existing_events.exists():
                messages.error(
                    request,
                    "An event already exists for this date."
                    "Please choose a different date."
                )
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

    else:
        form = BookingForm()

    return render(request, 'booking/new_booking.html', {'form': form})

@login_required
def booking_edit(request, pk):
    """
    View for editing booking
    """
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            new_booking_date = form.cleaned_data['date']

            existing_bookings = Booking.objects.filter(
                date=new_booking_date).exclude(pk=pk)

            # Check if the selected date is in the past
            if new_booking_date < timezone.now().date():
                messages.error(
                    request,
                    "You cannot create a booking in the past."
                    "Please choose a future date."
                )
                return redirect('booking:booking_list')

            # Check for conflicts with existing bookings
            if existing_bookings.exists():
                messages.warning(request, 'This date is already booked.')
                return redirect('booking:booking_list')

            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(event_date=new_booking_date)
            if existing_events.exists():
                messages.warning(
                    request,
                    "An event already exists for this date."
                    "Please choose a different date."
                )
                return redirect('booking:booking_list')

            booking = form.save(commit=False)
            booking.save()
            return redirect('booking:booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'booking/booking_list.html',
        {'form': form, 'booking': booking}
    )


@login_required
def booking_delete(request, number):
    """
    View for deleting booking
    """
    booking = get_object_or_404(Booking, number=number)
    booking.delete()
    return redirect('booking:booking_list')


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def staff_booking_list(request):
    """
    View for staff
    """
    now = datetime.now()
    upcoming_bookings = Booking.objects.filter(
        date__gte=datetime.now()).order_by('date', 'time')

    context = {
        'bookings': upcoming_bookings,
    }

    return render(request, 'booking/staff_list.html', context)
