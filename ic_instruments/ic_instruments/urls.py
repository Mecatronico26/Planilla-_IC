from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instruments/', include('instruments.urls')),  # Asegúrate de que esta línea esté presente
]