import django_filters
from .models import Course, Event

class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Course
        fields = ['name', 'start_date', 'end_date', 'price']

class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['name', 'date', 'location']
