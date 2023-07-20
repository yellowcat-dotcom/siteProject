from django.urls import path, include, re_path
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'meeting-rooms', MeetingRoomViewSet)

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

    # маршруты для Rest Framework
    path('api/configuration/', ConfigurationAPIView.as_view(), name='configuration_api'),
    path('api/', include(router.urls)),
    path('api/reservations/', ReservationListAPIView.as_view(), name='reservations-list'),
    path('api/reservations/<int:pk>/', ReservationDetailAPIView.as_view(), name='reservations-detail'),

    # для токенов
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))

]
