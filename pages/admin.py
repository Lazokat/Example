from django.contrib import admin
from .models import Blog
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body','created_at']
    list_filter = ['updated_at']

admin.site.register(Blog,PostAdmin)