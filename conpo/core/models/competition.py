from uuid import uuid4

from django.db import models

from conpo.core.models.event import Event


class Competition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    event = models.ForeignKey(Event, related_name='competitions')
    ctime = models.DateTimeField(auto_now_add=True, editable=False)
    slug = models.SlugField()
    name = models.CharField(max_length=128)
    published = models.BooleanField(default=False)
    results_published = models.BooleanField(default=False)

    class Meta:
        unique_together = (('event', 'slug'),)

    def __str__(self):
        return '{event}: {name}'.format(event=self.event, name=self.name)
