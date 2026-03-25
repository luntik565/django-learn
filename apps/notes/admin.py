from django.contrib import admin
from .models import Notes

@admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter = ['created_at', 'updated_date']
    readonly_fields = ('created_at', 'updated_date')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_date')
        })
    )