from django.db import models
from django.conf import settings
from datetime import datetime


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for event posts
    """
    title = models.CharField(
        max_length=30, verbose_name="Title")
    event_date = models.DateField(verbose_name="Date")
    event_description = models.TextField(
        max_length=130,
        default='Descripe the event here...'
    )
    event_location = models.CharField(
        max_length=50,
        default='Exampleway 123, 456 78, City'
    )
    featured_image = models.ImageField(
        blank=True,
        default='static/img/card-background.jpg'
    )
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
