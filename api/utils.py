from django_filters import rest_framework as filters
from .models import Game


def get_platforms_count(Model):
    answer = []
    model_obj = Model.objects.values('platform').distinct()
    lst = [name['platform'] for name in model_obj]
    for name in lst:
        count = Game.objects.filter(platform=name).count()
        answer.append({'platform': name, 'count': count})
    return answer


def get_genres_count(Model):
    answer = []
    model_obj = Model.objects.values('genre').distinct()
    lst = [name['genre'] for name in model_obj]
    for name in lst:
        count = Game.objects.filter(genre=name).count()
        answer.append({'genre': name, 'count': count})
    return answer


class GamesFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre', lookup_expr='iexact')
    platform = filters.CharFilter(field_name='platform', lookup_expr='iexact')
    year = filters.RangeFilter()

    class Meta:
        model = Game
        fields = ['genre', 'year', 'platform']





