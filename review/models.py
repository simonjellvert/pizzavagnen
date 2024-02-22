from django.db import models
from django.conf import settings
from user.models import CustomUser


class Review(models.Model):
    """ Reviews model """
    star_rate = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.CharField(
        max_length=20,
        choices=star_rate,
        default=1
    )
    content = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
