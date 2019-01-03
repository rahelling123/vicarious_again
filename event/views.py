from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import EventForm, CommentForm
from event.models import Event, Comment, Reply
from django.contrib.auth.decorators import login_required

# Create your views here.


def new_event(request):
    event_new = EventForm
    if request.method == 'POST':
        event_new = EventForm(data=request.POST)
        if event_new.is_valid():
            event = event_new.save(commit=False)
            event.author = request.user
            event.save()
            message = "Event succesfully saved!"
            context = {'message': message, 'event_new': event}
            return render(request, 'users/index.html', context)
        else:
            return HttpResponse("Form was not valid try again")
    else:
        context = {'form': event_new}

        return render(request, 'event/new_event.html', context)


def event_detail(request, event_id):
    detail_event = Event.objects.get(pk=event_id)
    comment_form = CommentForm
    comment_list = Comment.objects.filter(event=event_id)
    context = {'detail_event': detail_event, 'comment_form':comment_form, 'comment_list':comment_list}

    if request.method == 'POST':
        if request.POST['action']=='post comment':
            if not request.user.is_authenticated:
                return render(request, 'users/login.html', context)
            comment_new = CommentForm(data=request.POST)
            if comment_new.is_valid():
                comment = comment_new.save(commit=False)
                comment.author = request.user
                comment.event = detail_event
                comment.save()
                return HttpResponseRedirect('.')
            else:
                return HttpResponse("form not valid")
        elif request.POST['action'] == 'reply':
            reply_new = Reply(description=request.POST['reply'], author=request.user,
                              comment=Comment.objects.get(pk=request.POST['parent_id']))
            reply_new.save()
            return HttpResponseRedirect('.')

    else:
        return render(request, 'event/event_detail.html', context)

