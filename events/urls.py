from django.urls import path
from .views import PostList, add_post, edit_post


urlpatterns = [
    path('', PostList.as_view(), name='events'),
    path('events/add/', add_post, name='add_post'),
    path('events/<int:post_id>/edit/', edit_post, name='edit_post'),
]
