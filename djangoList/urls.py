from django.contrib import admin
from django.urls import path
import tasks.views as task_views

urlpatterns = [
    path('', task_views.index, name="home"),
    path('admin/', admin.site.urls),
]
