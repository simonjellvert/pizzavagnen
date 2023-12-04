from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from .forms import EventForm, EditEventForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class PostList(generic.ListView):
    model = Post
    template_name = 'events/events.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status=1, event_date__gte=timezone.now()).order_by('event_date')


@login_required
def add_post(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.title = "Some default title"
            event.save()
            return redirect('events')
    else:
        form = EventForm()

    return render(request, 'events/events.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == 'POST':
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EditEventForm(instance=event)

    return render(request, 'edit_post.html', {'form': form, 'event': event})
