from lepo.handlers import BaseHandler, ModelHandlerReadMixin

from conpo.api.schemata import CompetitionDetailSchema, CompetitionListSchema, EventSchema
from conpo.core.models import Competition, Event


class CompetitionHandler(ModelHandlerReadMixin, BaseHandler):
    model = Competition
    list_queryset = Competition.objects.filter(published=True, event__published=True)
    list_schema_class = CompetitionListSchema
    retrieve_queryset = list_queryset.select_related('event').prefetch_related('competitors')
    retrieve_schema_class = CompetitionDetailSchema


class EventHandler(ModelHandlerReadMixin, BaseHandler):
    model = Event
    list_queryset = Event.objects.filter(published=True).prefetch_related('competitions')
    schema_class = EventSchema


get_competition = CompetitionHandler.get_view('handle_retrieve')
list_competitions = CompetitionHandler.get_view('handle_list')
list_events = EventHandler.get_view('handle_list')
