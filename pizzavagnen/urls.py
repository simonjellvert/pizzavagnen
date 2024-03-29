"""pizzavagnen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import PostList
from django.conf import settings
from django.conf.urls.static import static

from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('events/', include('events.urls')),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls')),
    path('review/', include('review.urls')),
    path('booking/', include('booking.urls', namespace='booking'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'pizzavagnen.views.handler404'
handler500 = 'pizzavagnen.views.handler500'