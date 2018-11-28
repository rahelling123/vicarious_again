from django.http import HttpResponse
from django.shortcuts import render
from .forms import EventForm
from event.models import Event

# Create your views here.


def new_event(request):
    event_new = EventForm
    if request.method == 'POST':
        event_new = EventForm(data=request.POST)
        if event_new.is_valid():
            event = event_new.save()
            message = "Event succesfully saved!"
            context = {'message': message, 'event_new':event}
            return render(request, 'users/index.html', context)
        else:
            return HttpResponse("Form was not valid try again")
    else:
        context = {'form': event_new}
        return render(request, 'event/new_event.html', context)


def event_detail(request, event_id):
    detail_event = Event.objects.get(pk=event_id)
    context = {'detail_event': detail_event}
    return render(request, 'event/event_detail.html', context)