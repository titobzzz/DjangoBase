from django.shortcuts import render
from .models import Room
# from django.http import HttpResponse


rooms = Room.objects.all() 
print(rooms)

def home(request): 
    return render(request,'base/home.html', {'rooms' : rooms});


# pass a parameter 
def room(request,pk):
    room = Room.objects.get(id=pk)

    return render(request,'base/room.html', {'room': room});

# Create your views here.
