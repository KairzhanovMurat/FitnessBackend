from django.urls import path
from auth_app import views

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUsersView.as_view(), name='me'),
]
