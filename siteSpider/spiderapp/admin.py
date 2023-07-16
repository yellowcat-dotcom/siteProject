from django.contrib import admin
from .models import Department, Employee, MeetingRoom, Configuration, MeetingParticipant


class MeetingParticipantInline(admin.TabularInline):
    model = MeetingParticipant


class MeetingRoomAdmin(admin.ModelAdmin):
    inlines = [MeetingParticipantInline]


admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(MeetingRoom, MeetingRoomAdmin)
admin.site.register(Configuration)
