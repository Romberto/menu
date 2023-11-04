from django.contrib import admin

from .models import Menu, MenuItem


# Register your models here.
@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class AdminItemMenu(admin.ModelAdmin):
    pass



