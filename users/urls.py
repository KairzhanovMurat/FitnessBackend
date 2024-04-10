from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('trainers', views.TrainerViewSet)
router.register('regulars', views.RegularUserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

