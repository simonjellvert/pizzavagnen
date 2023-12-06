from django.urls import path
from .views import PostList, add_event, edit_event


urlpatterns = [
    path('', PostList.as_view(), name='events'),
    path('add/', add_event, name='add_event'),
    path('edit/<int:pk>/', edit_event, name='edit_event'),
]
