from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import TestModelForm, DirectMessageForm, DirectMessageReplyForm
from event.models import Event, Comment
from users.models import DirectMessage

# Create your views here.


def index(request):
    template_name = 'users/index.html'
    list_events = Event.objects.all().order_by('-id')[:6]
    context = {'list_events':list_events}
    return render(request,template_name, context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
            # the HttpResonseRedirect is there so the page does not ask to confirm
            # form resubmission after every time that you refresh the page
        else:
            return HttpResponse("form not valid try again")
    else:
        form = UserCreationForm
        context = {'form': form}
        template_name = 'users/signup.html'
    return render(request, template_name, context)

# TODO need to create a case that explains what is wrong if the form is not valid, spent a lot
# of time trying to figure out why the user was not saving, it was because i was not meeting requirements, but did not know it



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'users/logout.html')


#TODO when this fails it redirects anyways...
def login_view(request):
    list_events = Event.objects.all().order_by('-id')[:6]
    context = {'list_events':list_events}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse(index), context)
    else:
        return render(request, 'users/login.html')


#TODO need a logged in user dashboard and a non logged in user view
def dashboard(request, user_id):
    user = request.user
    if (user.is_authenticated and user.pk != user_id) or (not user.is_authenticated):
        return redirect('users:visitor', user_id=user_id)
    else:
        events = []
        user = request.user
        user_comment = Comment.objects.filter(author=user)
        #TODO this is not scalable is it?
        user_message = DirectMessage.objects.filter(recipient=user)
        for comment in user_comment:
            event_comment = comment.event
            if event_comment not in events:
                events.append(event_comment)
        context = {'user_comment':user_comment, 'events':events,
                   'user_message':user_message}
        return render(request, 'users/dashboard.html', context)


def test_model_view(request):
    form = TestModelForm
    if request.method == 'POST':
        example = TestModelForm(data=request.POST)
        if example.is_valid():
            mock_user = example.save()
            context = {'mock_user':mock_user}
            return render(request, 'users/index.html', context)
    else:
        context = {'form': form}
        return render(request,'users/testmodel.html', context)


def visitor(request, user_id):
    user_events= User.objects.get(pk=user_id).event_set.all()
    user_home = User.objects.get(pk=user_id)
    context = {'user_events':user_events, 'user_home':user_home}
    return render(request, 'users/visitor.html', context)


def direct_message_send(request, user_id):
    form = DirectMessageForm
    if request.method=='POST':
        new_direct_message = DirectMessageForm(data=request.POST)
        if new_direct_message.is_valid():
            new_direct_message = new_direct_message.save(commit=False)
            new_direct_message.sender = request.user
            new_direct_message.recipient = User.objects.get(pk=user_id)
            #TODO 3
            # new_direct_message.sender = request.user
            # new_direct_message.recipient = User.objects.get(pk=user_id)
            new_direct_message.save()
            #TODO pass this message in the redirect with context
            success = 'Message sent'
            return HttpResponseRedirect(reverse('users:visitor', args=[user_id],))
    else:
        context = {'form': form}
        return render(request, 'users/send_message.html', context)


#TODO 4
def thread(request, dm_id):
    form = DirectMessageReplyForm
    thread = DirectMessage.objects.get(pk=dm_id)
    thread_replies = thread.dm_reply.all()
    context = {'form':form, 'thread_replies':thread_replies}
    if request.method=='POST':
        new_reply = DirectMessageReplyForm(data=request.POST)
        if new_reply.is_valid():
            new_reply = new_reply.save(commit=False)
            new_reply.dm_reply = DirectMessage.objects.get(pk=dm_id) #TODO there has to be a better way to do this, doesnt this just create massive loops?
            new_reply.save()
            return HttpResponseRedirect(reverse('users:thread', args=[dm_id],))
    else:
        return render(request, 'users/thread.html', context)

