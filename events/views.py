from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from .forms import EventForm, EditEventForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from booking.models import Booking
from cloudinary.uploader import upload


class PostList(generic.ListView):
    model = Post
    template_name = 'events/events.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status=1, event_date__gte=timezone.now()).order_by('event_date')


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES.get('featured_image')
            response = cloudinary.uploader.upload(image)

            new_event_date = form.cleaned_data['event_date']
            # Check for conflicts with existing bookings
            existing_events = Post.objects.filter(event_date=new_event_date)
            if existing_events.exists():
                message = "An event already exists for this date. Please choose a different date."
                messages.warning(request, message)
                return redirect('events')
            
            # Check for conflicts with existing events in 'events' app
            existing_booking = Booking.objects.filter(date=new_event_date)
            if existing_booking.exists():
                messages.warning(request, 'This date is already booked.')
                return redirect('events')

            event = form.save(commit=False)
            event.user = request.user
            event.featured_image = response['url']
            event.status = 1
            event.save()
            return redirect('events')
        else:
            messages.error(
                request, 'Form submission failed. Please check the form.')
            print(form.errors)
    else:
        form = EventForm()

    return render(request, 'events/events.html', {'form': form})


@login_required
def edit_event(request, pk):
    event = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = EditEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            new_event_date = form.cleaned_data['event_date']

            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(
                event_date=new_event_date).exclude(pk=pk)
            if existing_events.exists():
                message = "An event already exists for this date. Please choose a different date."
                messages.warning(request, message)
                return redirect('events')

            # Check for conflicts with existing bookings
            existing_bookings = Booking.objects.filter(date=new_event_date)
            if existing_bookings.exists():
                messages.warning(request, 'This date is already booked.')
                return redirect('booking:booking_list')

            event = form.save(commit=False)
            event.save()
            return redirect('events')
    else:
        form = EditEventForm(instance=event)

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})
