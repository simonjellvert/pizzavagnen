from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = 'about.html'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status=1, event_time__gte=timezone.now()).order_by('_event_date')
