from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('authentication.urls')),
    path('api/admin/', include('authors.urls')),
    path('api/admin/', include('articles.urls')),
]
