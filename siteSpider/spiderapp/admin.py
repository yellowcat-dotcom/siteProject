from django.contrib import admin
from .models import Department
from .models import Employee
from .models import MeetingRoom
from .models import Configuration

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(MeetingRoom)
admin.site.register(Configuration)
