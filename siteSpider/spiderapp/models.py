from django.db import models
from solo.models import SingletonModel


class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)  # Отчество (может быть пустым)
    photo = models.ImageField(upload_to='employee_photos/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MeetingRoom(models.Model):
    number = models.CharField(max_length=10)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    has_tv = models.BooleanField()
    reserved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='reserved_rooms')
    participants = models.ManyToManyField(Employee, blank=True, related_name='meeting_rooms')
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.number


class Configuration(SingletonModel):
    address = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100)
    office_photo = models.ImageField(upload_to='office_photos/')

    def __str__(self):
        return self.address
