from uuid import uuid4

from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    ctime = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=128)
    published = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name
