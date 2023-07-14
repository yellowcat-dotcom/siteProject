from django.shortcuts import render, redirect, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView

from .models import Configuration, Department, Employee, MeetingRoom
from .serializers import ConfigurationSerializer, DepartmentSerializer, MeetingRoomSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, viewsets, mixins


def post_list(request):
    return render(request, 'spiderapp/post_list.html', {})


def configuration_view(request):
    configuration = Configuration.objects.get()
    return render(request, 'spiderapp/configuration.html', {'configuration': configuration})


def department_view(request):
    departments = Department.objects.all()
    return render(request, 'spiderapp/department.html', {'departments': departments})


def employee_view(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    department_id = request.GET.get('department')  # Получите выбранный отдел из параметров запроса
    reset = request.GET.get('reset')  # Получите параметр сброса фильтрации

    if reset:
        department_id = None  # Сбросить выбранный отдел

    return render(request, 'spiderapp/employee.html',
                  {'employees': employees, 'departments': departments, 'department_id': department_id})


def meetingRoom_view(request):
    meetingRooms = MeetingRoom.objects.all()
    return render(request, 'spiderapp/meetingRoom.html', {'meetingRooms': meetingRooms})


def booking_view(request, meeting_room_id):
    meeting_room = MeetingRoom.objects.get(id=meeting_room_id)
    employees = Employee.objects.all()  # Получить список всех работников

    if request.method == 'POST':
        reserved_by_id = request.POST.get('reserved_by')
        participants_ids = request.POST.getlist('participants')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # Получить объекты сотрудников и сохранить данные в БД
        reserved_by = Employee.objects.get(id=reserved_by_id)
        participants = Employee.objects.filter(id__in=participants_ids)

        meeting_room.reserved_by = reserved_by
        meeting_room.participants.set(participants)
        meeting_room.start_time = start_time
        meeting_room.end_time = end_time
        meeting_room.save()

        return redirect('meetingRooms')  # Перенаправление на список переговорных после сохранения

    context = {
        'meeting_room': meeting_room,
        'employees': employees,
    }

    return render(request, 'spiderapp/booking.html', context)


def edit_booking_view(request, meeting_room_id):
    meeting_room = get_object_or_404(MeetingRoom, id=meeting_room_id)
    employees = Employee.objects.all()

    if request.method == 'POST':
        reserved_by_id = request.POST.get('reserved_by')
        participants_ids = request.POST.getlist('participants')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        reserved_by = get_object_or_404(Employee, id=reserved_by_id)
        participants = Employee.objects.filter(id__in=participants_ids)

        meeting_room.reserved_by = reserved_by
        meeting_room.participants.set(participants)
        meeting_room.start_time = start_time
        meeting_room.end_time = end_time
        meeting_room.save()

        return redirect('meetingRooms')

    context = {
        'meeting_room': meeting_room,
        'employees': employees,
        'selected_participants': meeting_room.participants.all(),  # Добавлено
    }

    return render(request, 'spiderapp/edit_booking.html', context)


def delete_booking_view(request, meeting_room_id):
    meeting_room = get_object_or_404(MeetingRoom, id=meeting_room_id)
    meeting_room.reserved_by = None
    meeting_room.participants.clear()
    meeting_room.start_time = None
    meeting_room.end_time = None
    meeting_room.save()
    return redirect('meetingRooms')


def filter_employees(request):
    department_id = request.GET.get('department')  # Получаем значение поля department из запроса
    employees = Employee.objects.all()

    if department_id:
        employees = employees.filter(department_id=department_id)  # Фильтрация сотрудников по значению department_id

    context = {
        'employees': employees,
    }

    return render(request, 'spiderapp/employee.html', context)


# представления для Rest Framework
class ConfigurationAPIView(APIView):
    def get(self, request):
        configurations = Configuration.objects.all()
        serializer = ConfigurationSerializer(configurations, many=True)
        return Response(serializer.data)

    # нужен ли вообще тут метод post
    # def post(self, request):
    #     serializer = ConfigurationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)


class DepartmentListAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# было в прошлый раз
# class MeetingRoomListAPIView(APIView):
#
#     def get(self, request):
#         meeting_rooms = MeetingRoom.objects.all()
#         serializer = MeetingRoomSerializer(meeting_rooms, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = MeetingRoomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# стало
class MeetingRoomListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# было в прошлый раз

# class MeetingRoomDetailAPIView(APIView):
#     def get(self, request, pk):
#         meeting_room = MeetingRoom.objects.get(pk=pk)
#         serializer = MeetingRoomSerializer(meeting_room)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         meeting_room = MeetingRoom.objects.get(pk=pk)
#         serializer = MeetingRoomSerializer(meeting_room, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         meeting_room = MeetingRoom.objects.get(pk=pk)
#         meeting_room.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class MeetingRoomDetailAPIView(GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                               mixins.RetrieveModelMixin):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class EmployeeListAPIView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# использую viewset
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department']
