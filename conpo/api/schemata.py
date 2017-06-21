from marshmallow import fields, Schema


class CompetitorSchema(Schema):
    name = fields.String(attribute='display_name')
    position = fields.Integer()


class CompetitionListSchema(Schema):
    class Meta:
        additional = ('id', 'name', 'slug', 'results_published')


class CompetitionDetailSchema(CompetitionListSchema):
    event = fields.Nested('EventSchema', exclude=('competitions',))
    competitors = fields.Method('get_competitors')

    def get_competitors(self, obj):
        # See https://github.com/marshmallow-code/marshmallow/issues/430
        exclude = (('position',) if not obj.results_published else ())
        competitors = sorted(obj.competitors.all(), key=lambda c: (c.position or 0xFFFFFFF, c.display_name))
        return CompetitorSchema(exclude=exclude).dump(competitors, many=True).data


class EventSchema(Schema):
    competitions = fields.Method('get_competitions')

    class Meta:
        additional = ('id', 'name', 'slug')

    def get_competitions(self, obj):
        # See https://github.com/marshmallow-code/marshmallow/issues/430
        # This uses a list comprehension to make prefetch viable.
        competitions = [c for c in obj.competitions.all() if c.published]
        return CompetitionListSchema().dump(competitions, many=True).data
