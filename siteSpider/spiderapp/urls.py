from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'employees', EmployeeViewSet)

routerEmployees = routers.DefaultRouter()
routerEmployees.register(r'employees', EmployeeViewSet)

routerDepartments = routers.DefaultRouter()
routerDepartments.register(r'departments', DepartmentViewSet)

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
    # path('api/departments/', DepartmentListAPIView.as_view(), name='department-list'),
    # path('api/departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),

    # использую viewset path('api/departments/', DepartmentViewSet.as_view({'get': 'list'})),
    # path('api/departments/<int:pk>/', DepartmentViewSet.as_view({'put': 'update', 'get': 'retrieve',
    # 'delete': 'destroy'})),

    path('api/', include(routerDepartments.urls)),
    path('api/meeting-rooms/', MeetingRoomListAPIView.as_view(), name='meeting-rooms-list'),
    path('api/meeting-rooms/<int:pk>/', MeetingRoomDetailAPIView.as_view(), name='meeting-room-detail'),

    # path('api/employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    # path('api/employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),

    # использую viewset
    # path('api/employees/', EmployeeViewSet.as_view({'get': 'list'})),
    # path('api/employees/<int:pk>/', EmployeeViewSet.as_view({'put': 'update'})),

    # использование SimpleRouter
    path('api/', include(routerEmployees.urls)),
]
