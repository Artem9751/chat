from django.shortcuts import render
from django.utils import timezone
#from django.http import HttpResponseRedirect
from .models import Message

def HomePageView(request):
    message_list = Message.objects.order_by('-message_time')[:5]
    text = request.POST.get('text')
    author = request.POST.get('name')
    #Message.objects.create(message_text = text, message_author = author, message_time = timezone.now())
    new_message = Message(message_text = text, message_author = author, message_time = timezone.now())
    new_message.save()
    return render(request, 'home.html', {'message_list': message_list})

