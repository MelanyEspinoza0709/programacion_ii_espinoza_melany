from django.contrib import admin
from .models import Project, Estacionamiento


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    
@admin.register(Estacionamiento)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at", "dirección", "capacidad_total", "espacios_disponibles")
    search_fields = ("nombre",)