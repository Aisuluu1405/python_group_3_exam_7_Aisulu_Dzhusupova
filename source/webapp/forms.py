from django import forms
from django.forms import widgets
from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        exclude = ['created']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'poll']


class PollChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['poll']
