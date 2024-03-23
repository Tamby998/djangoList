from django.contrib import admin
from django.urls import path
import tasks.views as task_views

urlpatterns = [
    path('', task_views.index, name="home"),
    path('add-collection/', task_views.add_collection, name="add-collection"),
    path('add-task/', task_views.add_task, name="add-task"),
    path('delete-task/<int:task_pk>/', task_views.delete_task, name="delete-task"),
    path('delete-collection/<int:collection_pk>/', task_views.delete_collection, name="delete-collection"),
    path('get-tasks/<int:collection_pk>/', task_views.get_tasks, name="get-tasks"),
    path('admin/', admin.site.urls),
]
