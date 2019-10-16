from django import forms

from django.utils.translation import gettext_lazy

from .models import Message

class MessageForm(forms.Form):
    model = Message
    message = forms.CharField(widget=forms.Textarea)