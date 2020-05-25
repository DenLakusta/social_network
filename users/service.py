from django_filters import rest_framework as filters
from likes.models import Like



class LikeFilter(filters.FilterSet):

    date = filters.RangeFilter()

    class Meta:
        model = Like
        fields = ['date',]