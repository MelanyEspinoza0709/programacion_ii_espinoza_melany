from django.contrib import admin
from .models import Project, Estacionamiento, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    
@admin.register(Estacionamiento)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at", "dirección", "capacidad_total", "espacios_disponibles")
    search_fields = ("nombre",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filter = ("status", "project")
    search_fields = ("title", "description")