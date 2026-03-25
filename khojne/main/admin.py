"""
Django admin configuration for Khoj Sewa.
"""
from django.contrib import admin
from .models import Service, ServiceRequest


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'phone', 'created_at')
    list_filter = ('type', 'location')
    search_fields = ('name', 'phone')


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location', 'status', 'created_at')
    list_filter = ('type', 'location', 'status')
    search_fields = ('name', 'problem')
