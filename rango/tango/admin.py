from django.contrib import admin
from .models import Category , Page
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page , PageAdmin)
