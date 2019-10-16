from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Message
from django.views.generic import ListView
from .forms import MessageForm
from django.views.generic.edit import CreateView

'''
def HomePageView(request):
    message_list = Message.objects.order_by('-message_time')[:5]
    if request.method == "GET":
        return render(request, 'home.html', {'message_list': message_list})
    elif request.method == "POST":
        text = request.POST.get('text')
        author = request.POST.get('name')
        #Message.objects.create(message_text = text, message_author = author, message_time = timezone.now())
        new_message = Message(message_text = text, message_author = author, message_time = timezone.now())
        new_message.save()
        return render(request, 'home.html', {'message_list': message_list})
'''

class HomePageView(ListView):
    #template_name = 'home.html'
    #model = Message
    #context_object_name = 'message_list'
    #form_class = MessageForm

    def get(self, request):
        return self.render(request)


    def post(self, request):
        text = request.POST.get('text')
        author = request.POST.get('name')
        new_message = Message(message_text=text, message_author=author, message_time=timezone.now())
        new_message.save()
        return self.render(request)

    def render(self, request):
        message_list = Message.objects.order_by('-message_time')[:5]
        return render(request, 'home.html', {'message_list': message_list})