import pytest

from conpo.core.models import Event


@pytest.mark.django_db
@pytest.fixture
def event():
    return Event.objects.create(name='Demo Event', slug='demo-event', published=True)
