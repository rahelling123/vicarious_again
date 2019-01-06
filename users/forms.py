# forms can go here

from django.forms import ModelForm
from .models import TestModel, DirectMessage, DirectMessageReply


class TestModelForm(ModelForm):
    class Meta:
        model = TestModel
        fields = ['name', 'last', 'username']


class DirectMessageForm(ModelForm):
    class Meta:
        model = DirectMessage
        fields = ['content']


class DirectMessageReplyForm(ModelForm):
    class Meta:
        model = DirectMessageReply
        fields = ['content']