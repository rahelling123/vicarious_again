from django.forms import ModelForm
from .models import Event
from django.contrib.auth.decorators import login_required

#all forms below


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description']