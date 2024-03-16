from django.contrib import admin
from django.urls import path
import tasks.views as task_views

urlpatterns = [
    path('', task_views.index, name="home"),
    path('add-collection/', task_views.add_collection, name="add-collection"),
    path('add-task/', task_views.add_task, name="add-task"),
    path('get-tasks/<int:collection_pk>/', task_views.get_tasks, name="get-tasks"),
    path('admin/', admin.site.urls),
]
