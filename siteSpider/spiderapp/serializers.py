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

    def validate_name(self, value):
        if Department.objects.filter(name=value).exists():
            raise serializers.ValidationError("Отдел с таким названием уже существует.")
        return value

    def validate_floor(self, value):
        if value < 0:
            raise serializers.ValidationError('Значение этажа не может быть отрицательным.')
        return value


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


class MeetingRoomDetailSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        many=True,
        required=False
    )

    def validate(self, attrs):
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        if start_time and end_time:
            if start_time > end_time:
                raise serializers.ValidationError('Время окончания раньше времени начала')
            if start_time < timezone.now():
                raise serializers.ValidationError('Время начала уже прошло')
        else:
            raise serializers.ValidationError('Необходимо указать и время начала, и время окончания')

        return attrs

    def validate_participants(self, value):
        room_capacity = self.instance.capacity if self.instance else self.initial_data.get('capacity', 0)
        if len(value) > room_capacity - 1:
            raise serializers.ValidationError("Количество участников превышает вместимость переговорной комнаты.")
        return value

    class Meta:
        model = MeetingRoom
        fields = ['reserved_by', 'participants', 'start_time', 'end_time']




class MeetingRoomPostAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ['number', 'floor', 'capacity', 'has_tv']

    def validate_number(self, value):
        if MeetingRoom.objects.filter(number=value).exists():
            raise serializers.ValidationError("Переговорная с таким номером уже существует.")
        return value

    # def validate_floor(self, value):
    #     if value < 0:
    #         raise serializers.ValidationError('Значение этажа не может быть отрицательным.')
    #     return value

    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError('Значение вместимости не может быть отрицательным.')
        return value
