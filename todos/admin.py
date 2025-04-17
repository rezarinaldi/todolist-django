from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'created_at', 'updated_at')

# admin.site.register(Todo, TodoAdmin)
