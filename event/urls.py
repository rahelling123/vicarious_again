from django.conf.urls import url
from django.urls import path
from .views import new_event, event_detail

app_name = 'event'
urlpatterns = [
    path('new_event/', new_event, name='new_event'),
    path('event_detail/<int:event_id>/', event_detail, name='event_detail')
]