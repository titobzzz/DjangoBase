from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User



def loginPage(request):
    if request.method == "POST":
        print(request.method)
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username) 
        except:
            messages.error(request, "username does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
             login(user)          
             return redirect('home')
        else:
            messages.error(request, "username and password not correct")
        
    context={}
    return render(request, 'base/login_register.html', context)

def logOut(request):
    logout(request)
    return redirect('home')

def home(request): 
    q = request.GET.get('q') if request.GET.get('q') != None else ''
   
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)  |
        Q(description__icontains=q) )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context={
        'rooms' : rooms,
        'topics':topics,
        'room_count':room_count
        }
    return render(request,'base/home.html', context );


# pass a parameter 
def room(request,pk):
    room = Room.objects.get(id=pk)

    return render(request,'base/room.html', {'room': room});


def createRoom(request):

    form = RoomForm()     
#have a form and check if its is a POST request then
    if request.method == 'POST':
        # pass all the POST request into form(RoomForm)
        form =  RoomForm(request.POST)
        # check if the form is valid  if so save and redirect
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form': form}
    return render(request, 'base/room_form.html', context )
# Create your views here.


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room )
        
        if form.is_valid: 
            form.save()
            print(form)
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request,pk):
    
    room = Room.objects.get(id=pk)
  #if request type is POST then delete
    if request.method == 'POST':
       room.delete()
       return redirect('home')
      
    return render(request, 'base/delete.html',{'obj': room})