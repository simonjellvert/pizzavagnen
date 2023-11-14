from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import translation, formats
from django.utils.timezone import make_aware
from datetime import datetime


STATUS = ((0, "Utkast"), (1, "Publicera"))


class Post(models.Model):
    title = models.CharField(
        max_length=200, unique=True, verbose_name="Rubrik")
    event_date = models.DateField(verbose_name="Datum")
    featured_image = CloudinaryField(
        'Bild',
        default='placeholder',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="event_posts",
        name="Signerat"
    )
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "Posts"

    def formatted_event_date(self):
        current_language = translation.get_language()
        translation.activate("sv")

        # Set the language for the current thread
        with translation.override("sv"):
            event_date_as_datetime = make_aware(datetime.combine(
                self.event_date, datetime.min.time()))
            formatted_date = formats.date_format(
                event_date_as_datetime, "DATE_FORMAT")

        translation.activate(current_language)

        return f"Den {formatted_date}"

    def __str__(self):
        return self.title
