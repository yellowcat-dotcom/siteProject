from rest_framework import serializers
from .models import Configuration, Department, MeetingRoom, Employee


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'address', 'working_hours', 'office_photo']  # что будем возвращать обратно клиенту


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'floor']


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ['id', 'number', 'floor', 'capacity', 'has_tv', 'reserved_by', 'participants', 'start_time', 'end_time']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'department']
