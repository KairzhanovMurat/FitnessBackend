from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('gyms/', include('gyms.urls')),
    path('users/', include('users.urls')),
    path('schedules/', include('schedules.urls')),
    path('staff/', include('staff.urls'))
]

urlpatterns += [
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('',
         SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
]
