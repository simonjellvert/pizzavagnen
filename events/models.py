from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Utkast"), (1, "Publicera"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Rubrik")
    slug = models.SlugField(max_length=200, unique=True)
    event_date = models.DateField(verbose_name="Datum")
    content = models.TextField(verbose_name="Innehåll")
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
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    