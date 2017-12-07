from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Advert(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(null=False, blank=False, default=now)

