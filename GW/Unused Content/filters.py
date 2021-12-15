import django_filters
from django_filters import CharFilter

from .models import *

class MonthsFilter(django_filters.FilterSet):

    class Meta:
        model = Months
        fields = ['State', 'Year', ]