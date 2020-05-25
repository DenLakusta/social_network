from django_filters import rest_framework as filters
from likes.models import Like



class LikeFilter(filters.FilterSet):

    date_start = filters.RangeFilter()
    date_to = filters.RangeFilter()

    class Meta:
        model = Like
        fields = ['date_start', 'date_to']