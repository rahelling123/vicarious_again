from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import TestModelForm
from event.models import Event, Comment

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return render(request, 'users/index.html')
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
        for comment in user_comment:
            event_comment = comment.event
            if event_comment not in events:
                events.append(event_comment)
        context = {'user_comment':user_comment, 'events':events}
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
    return render(request, 'users/visitor.html')




