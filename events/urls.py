from django.urls import path
from .views import PostList, add_event, edit_event, event_delete


urlpatterns = [
    path('', PostList.as_view(), name='events'),
    path('add/', add_event, name='add_event'),
    path('events/edit/<int:pk>/', edit_event, name='edit_event'),
    path('events/delete/<int:post_id>/', event_delete, name='event_delete'),
]
