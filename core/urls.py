from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as pattern

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
]

urlpatterns += pattern
