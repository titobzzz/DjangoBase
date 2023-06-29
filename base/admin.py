from django.contrib import admin
from .models import Room



# class RoomAdmin(admin.ModelAdmin):
#     list_display = (','name','description','created',)

admin.site.register(Room)
# # Register your models here.
