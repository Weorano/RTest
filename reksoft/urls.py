from django.contrib import admin
from django.urls import path, include

from mainapp.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # -----------------------------------------------------------------------------------------------------------------
    # Основные страницы
    # -----------------------------------------------------------------------------------------------------------------
    path('', index_view, name='Главная'),
]