import pytest

from conpo.testing.data import create_competition
from conpo.testing.utils import get_data_from_response


@pytest.mark.django_db
def test_nonpublished_compos_do_not_appear_in_lists(client, event):
    compo = create_competition(event, competition_data=dict(published=False))
    assert get_data_from_response(client.get('/api/v0/competitions')) == []


@pytest.mark.django_db
@pytest.mark.xfail(reason='404 handling is not robust yet')
def test_nonpublished_compos_are_not_accessible(client, event):
    compo = create_competition(event, competition_data=dict(published=False))
    assert get_data_from_response(client.get('/api/v0/competition/{id}'.format(id=compo.id))) == []


@pytest.mark.django_db
def test_published_compos_do_appear_in_lists(client, event):
    compos = [create_competition(event, competition_data=dict(published=True)) for x in range(5)]
    for compos_data in (
        get_data_from_response(client.get('/api/v0/competitions')),
        get_data_from_response(client.get('/api/v0/events'))[0]['competitions'],
    ):
        assert len(compos_data) == len(compos)
        assert set(c['id'] for c in compos_data) == set(str(c.id) for c in compos)


@pytest.mark.django_db
def test_compo_detail_does_not_crash(client, event):
    compo = create_competition(event)
    data = get_data_from_response(client.get('/api/v0/competition/{id}'.format(id=compo.id)))
