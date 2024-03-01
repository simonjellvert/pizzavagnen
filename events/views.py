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


class PostList(generic.ListView):
    """ Function for displaying a list of future events """
    model = Post
    template_name = 'events/events.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status=1, event_date__gte=timezone.now()).order_by('event_date')


@login_required
def add_event(request):
    """ Create new event as staff """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Your event was successfully posted!')
            new_event_date = form.cleaned_data['event_date']

            # Check if the selected date is in the past
            if new_event_date < timezone.now().date():
                messages.error(request, 'Cannot book a date in the past.')
                return redirect('events')

            # Check for conflicts with existing bookings
            existing_events = Post.objects.filter(event_date=new_event_date)
            if existing_events.exists():
                messages.error(
                    request,
                    "An event already exists for this date."
                    "Please choose a different date.")
                return redirect('events')

            # Check for conflicts with existing events in 'events' app
            existing_booking = Booking.objects.filter(date=new_event_date)
            if existing_booking.exists():
                messages.error(
                    request,
                    'This date is already booked.'
                    'Please choose a different date.'
                )
                return redirect('events')

            event = form.save(commit=False)
            event.user = request.user
            event.status = 1
            event.save()
            return redirect('events')
        else:
            messages.error(
                request, 'Something went wrong. All fields must be valid')
            posts = Post.objects.filter(
                status=1, event_date__gte=timezone.now()
            ).order_by('event_date')
    else:
        form = EventForm()
        posts = Post.objects.filter(
            status=1, event_date__gte=timezone.now()).order_by('event_date')

    return render(
        request, 'events/events.html', {'form': form, 'post_list': posts}
    )


@login_required
def edit_event(request, pk):
    """ Edit event as staff """
    event = get_object_or_404(Post, pk=pk)
    posts = Post.objects.filter(
        status=1, event_date__gte=timezone.now()).order_by('event_date')

    if request.method == 'POST':
        form = EditEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            messages.success(request, 'Your event is updated!')
            new_event_date = form.cleaned_data['event_date']

            # Check if the selected date is in the past
            if new_event_date < timezone.now().date():
                messages.error(
                    request,
                    'Cannot book a date in the past.'
                    'Please choose a different date.'
                )
                return redirect('events')

            # Check for conflicts with existing events in 'events' app
            existing_events = Post.objects.filter(
                event_date=new_event_date).exclude(pk=pk)
            if existing_events.exists():
                messages.error(
                    request,
                    "An event already exists for this date."
                    "Please choose a different date.")
                return redirect('events')

            # Check for conflicts with existing bookings
            existing_bookings = Booking.objects.filter(date=new_event_date)
            if existing_bookings.exists():
                messages.error(
                    request,
                    'This date is already booked.'
                    'Please choose a different date.'
                )
                return redirect('events')

            event = form.save(commit=False)
            event.save()
            return redirect('events')
        else:
            form = EditEventForm(instance=event)
            posts = Post.objects.filter(
                status=1, event_date__gte=timezone.now()
            ).order_by('event_date')
            messages.error(
                request, 'Something went wrong. All fields must be valid'
            )

    return render(
        request,
        'events/events.html',
        {'form': form, 'event': event, 'post_list': posts}
    )


@login_required
def event_delete(request, post_id):
    """ Delete event as staff """
    event = get_object_or_404(Post, id=post_id)
    event.delete()
    messages.success(request, 'Your event was successfully deleted!')
    return redirect('events')
