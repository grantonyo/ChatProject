from django.shortcuts import render, redirect
from .models import Room, Message

def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        # print('Username is ', username, ". Room name is: ", room)

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')

def MessageView(request, room_name, username):
    # print('Post result in message view: 1) Username is ', username, "2) Room name is: ", room_name)

    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']
        print("Posted message is", message)
        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)
    context = {
        'messages': get_messages,
        'user': username
    }
    return render(request, 'message.html', context)
