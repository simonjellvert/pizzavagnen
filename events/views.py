from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = 'events/events.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status=1, event_date__gte=timezone.now()).order_by('event_date')

