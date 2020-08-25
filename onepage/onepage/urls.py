from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('modelling/', include('modelling.urls')),
    path('admin/', admin.site.urls),
]
