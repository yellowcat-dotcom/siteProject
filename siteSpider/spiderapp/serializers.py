from django.utils import timezone
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


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'department']


class MeetingRoomSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    reserved_by = serializers.SerializerMethodField()

    def get_participants(self, obj):
        participants = obj.participants.all()
        reserved_by = obj.reserved_by
        participant_list = []
        for participant in participants:
            if participant != reserved_by:
                participant_list.append(participant.last_name + ' ' + participant.first_name)
        return participant_list

    def get_reserved_by(self, obj):
        reserved_by = obj.reserved_by
        if reserved_by:
            return f"{reserved_by.last_name} {reserved_by.first_name} {reserved_by.middle_name}"
        return None

    class Meta:
        model = MeetingRoom
        fields = ['id', 'number', 'floor', 'capacity', 'has_tv', 'reserved_by', 'participants', 'start_time',
                  'end_time']


class MeetingRoomCreateSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = MeetingRoom
        fields = ['id', 'number', 'floor', 'capacity', 'has_tv', 'reserved_by', 'participants', 'start_time',
                  'end_time']

    def validate(self, attrs):
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')
        if start_time > end_time:
            raise serializers.ValidationError('Время окончание раньше времени начала')
        if start_time < timezone.now():
            raise serializers.ValidationError('Вреимя начала уже прошло')
        return attrs