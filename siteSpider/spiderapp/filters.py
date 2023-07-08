import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department__name', lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['department']
