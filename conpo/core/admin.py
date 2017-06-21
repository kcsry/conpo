from django.contrib import admin

from conpo.core.models import Competition, Competitor, Event

admin.site.register((Competition, Competitor, Event))
