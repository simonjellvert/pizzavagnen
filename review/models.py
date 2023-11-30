from django.db import models
from django.conf import settings
from user.models import User


class Review(models.Model):
    """
    Reviews model
    """
    STAR_RATE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.CharField(
        max_length=20,
        choices=STAR_RATE,
        default=1
    )
    content = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
