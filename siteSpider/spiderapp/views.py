from django.shortcuts import render
from .models import Configuration, Department, Employee, MeetingRoom


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
    return render(request, 'spiderapp/employee.html', {'employees': employees})


def meetingRoom_view(request):
    meetingRooms = MeetingRoom.objects.all()
    return render(request, 'spiderapp/meetingRoom.html', {'meetingRooms': meetingRooms})

