from django.urls import path
from . import views
from .views import configuration_view, department_view, employee_view, meetingRoom_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('configuration/', configuration_view, name='configuration'),
    path('departments/', department_view, name='departments'),
    path('employees/', employee_view, name='employees'),
    path('meetingRooms/', meetingRoom_view, name='meetingRooms'),
    path('booking/<int:meeting_room_id>/', views.booking_view, name='booking'),
    path('edit_booking/<int:meeting_room_id>/', views.edit_booking_view, name='edit_booking'),
    path('delete_booking/<int:meeting_room_id>/', views.delete_booking_view, name='delete_booking'),
    path('filter_employees/', views.filter_employees, name='filter_employees'),
]