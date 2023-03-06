from django_filters import rest_framework as filters
from .models import Game


def get_platforms_count(Model):
    """
    return count games for ours platform
    """
    answer = []
    model_obj = Model.objects.values('platform').distinct()
    lst = [name['platform'] for name in model_obj]
    for name in lst:
        count = Game.objects.filter(platform=name).count()
        answer.append({'platform': name, 'count': count})
    return answer


def get_genres_count(Model):
    """
    return count games for ours genre
    """
    answer = []
    model_obj = Model.objects.values('genre').distinct()
    lst = [name['genre'] for name in model_obj]
    for name in lst:
        count = Game.objects.filter(genre=name).count()
        answer.append({'genre': name, 'count': count})
    return answer


class GamesFilter(filters.FilterSet):
    """
    Creating a filterSet for GET requests to filter data
    Search data by genre name in GET request: genre=sports
    Search data by platform name in GET request: platform=wii
    Search for a year in a range period in GET request: year_min=1998&year_max=2009
    Queries are case-insensitive.

    An example of a request:
        ?genre=racing&platform=ps&year_min=1998&year_max=2020

    """
    genre = filters.CharFilter(field_name='genre', lookup_expr='iexact')
    platform = filters.CharFilter(field_name='platform', lookup_expr='iexact')
    year = filters.RangeFilter()

    class Meta:
        model = Game
        fields = ['genre', 'year', 'platform']
