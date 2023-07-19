from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.db.models import Q
from .models import Room, Topic, Message
from .forms import RoomForm
from django.contrib.auth.models import User



def loginPage(request):
   
    page='loginPage'
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
            print("USER",user)
        except:
            messages.error(request, "username does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
             login(request, user)          
             return redirect('home')
        else:
            messages.error(request, "username and password not correct")
        
    context={'form':page}
    return render(request, 'base/login_register.html', context)



def logOut(request):
    logout(request)
    return redirect('home')



def registerPage(request):
   form = UserCreationForm()

   if request.method == 'POST':
     form = UserCreationForm(request.POST)
     if form.is_valid():
         user = form.save(commit=False)
         user.username = user.username.lower()
         user.save()
         login(request,user)
         return redirect('home')
     else:
         messages.error(request, "an error occured")

   return render(request,'base/login_register.html',{'form':form})



def home(request): 
    q = request.GET.get('q') if request.GET.get('q') != None else ''
   
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)  |
        Q(description__icontains=q) )

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context={
        'rooms' : rooms,
        'topics':topics,
        'room_count':room_count,
        'room_messages':room_messages
        }
    return render(request,'base/home.html', context )




# pass a parameter 
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        #propertiy of users creating a message
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {
        'room': room,
        'room_messages':room_messages,
        'participants': participants
        }
    return render(request,'base/room.html',context );



@login_required(login_url='loginPage')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message= user.message_set.all()
    topics= Topic.objects.all()

    context={
        'user':user,
        'rooms':rooms,
        'room_messages': room_message,
        'topics':topics
        }
    return render(request,'base/profile.html',context)



@login_required(login_url='loginPage')
def createRoom(request):

    form = RoomForm()    
#have a form and check if its is a POST request then
    if request.method == 'POST':
        # pass all the POST request into form(RoomForm)
        form =  RoomForm(request.POST)
        # check if the form is valid  if so save and redirect
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            return redirect('home')
        
    context={'form': form}
    return render(request, 'base/room_form.html', context )
# Create your views here.




@login_required(login_url='loginPage')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('only host can edit room')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room )
        
        if form.is_valid: 
            form.save()
            print(form)
            return redirect('home')

    context= {'form': form}
    return render(request, 'base/room_form.html',context)



@login_required(login_url='loginPage')
def deleteRoom(request,pk):
    
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('only host can edit room')
    
  #if request type is POST then delete
    if request.method == 'POST':
       room.delete()
       return redirect('home')
      
    return render(request, 'base/delete.html',{'obj': room})


@login_required(login_url='loginPage')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('only sender delete messages')
    
  #if request type is POST then delete
    if request.method == 'POST':
       message.delete()
       return redirect('home')
      
    return render(request, 'base/delete.html',{'obj':message})






