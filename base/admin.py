from django.contrib import admin
from .models import Room, Topic , Message 



# class RoomAdmin(admin.ModelAdmin):
#     list_display = (','name','description','created',)

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
# # Register your models here.
