from django.forms import ModelForm
from .models import Event, Comment
from django.contrib.auth.decorators import login_required

#all forms below


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']