from random import choice, randint, sample

from django.utils.crypto import get_random_string
from django.utils.text import slugify

from conpo.core.models import Competition, Competitor


def generate_gibberish():
    return get_random_string(randint(5, 15), 'pipapo mimamo riraro').strip().title()


def extend(*dicts):
    target = dicts[0]
    for dict in dicts[1:]:
        target.update(dict)
    return target


def create_competition(event, competition_data={}, n_competitors=None, positions=True):
    name = generate_gibberish()
    competition_data = extend(dict(
        event=event,
        name=name,
        slug=slugify(name),
        published=True,
        results_published=(randint(0, 100) < 50),
    ), competition_data)
    competition = Competition.objects.create(**competition_data)
    if n_competitors is None:
        n_competitors = randint(3, 15)
    if n_competitors > 0:
        competitors = [
            Competitor.objects.create(competition=competition, display_name=generate_gibberish())
            for i in range(n_competitors)
        ]
        if positions:
            winners = sample(competitors, min(len(competitors), choice([1, 3, 5])))
            for position, competitor in enumerate(winners, 1):
                competitor.position = position
                competitor.save()
    return competition
