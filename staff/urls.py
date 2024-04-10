from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

staff_router = DefaultRouter()
staff_router.register(r'gyms', views.GymCreateUpdateDeleteViewSet)
staff_router.register(r'schedules', views.ScheduleCreateUpdateDeleteViewSet)
urlpatterns = [
    path('manage/', include(staff_router.urls)),
]
