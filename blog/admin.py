from django.contrib import admin

from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    list_display = ('title', 'created_time', 'author', 'category', 'status')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Category)