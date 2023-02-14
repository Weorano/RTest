from django.contrib import admin
from django.urls import path, include

from quarry.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    # -----------------------------------------------------------------------------------------------------------------
    # Основные страницы
    # -----------------------------------------------------------------------------------------------------------------
    path('', IndexView.as_view(), name='Главная'),
]
