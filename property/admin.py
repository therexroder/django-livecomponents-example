from django.contrib import admin

from property.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "city", "created_at")
    search_fields = ("title", "city")
