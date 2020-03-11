import django_filters
from django_filters import DateFilter, NumberFilter
from django import forms

from .models import Alert

class AlertFilter(django_filters.FilterSet):
    id__gt = NumberFilter(field_name='id',lookup_expr='gte')
    id__lt = NumberFilter(field_name='id',lookup_expr='lte')
    Affiliate_Code = django_filters.CharFilter(lookup_expr='icontains')
    Exception_Category = django_filters.CharFilter(lookup_expr='icontains')
    start_date = DateFilter(field_name="Date_Discovered", lookup_expr='gte', input_formats=['%d/%m/%Y %H:%M'])
    end_date = DateFilter(field_name="Date_Discovered", lookup_expr='lte')

    class Meta:
        model = Alert
        fields = ['Acccount_Number','msisdn','id','Exception_Category','Affiliate_Code','Date_Discovered']
      