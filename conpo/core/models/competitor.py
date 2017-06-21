from uuid import uuid4

from django.db import models

from conpo.core.models.competition import Competition


class Competitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    competition = models.ForeignKey(Competition, related_name='competitors')
    display_name = models.CharField(max_length=128)
    position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.display_name
