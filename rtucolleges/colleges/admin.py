from django.contrib import admin

from .models import College


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('title', 'verified', 'establishment_date')
    search_fields = ['title']
