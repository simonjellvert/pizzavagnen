from django.urls import path
from .views import review_list, review_create, review_edit, review_delete

urlpatterns = [
    path('list/', review_list, name='review_list'),
    path('create/', review_create, name='review_create'),
    path('<int:pk>/edit/', review_edit, name='review_edit'),
    path('<int:review_id>/delete/', review_delete, name='review_delete'),
]
