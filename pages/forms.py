from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Create forms of the topic model."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Create forms of the the Entry model."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widegts = {'text': forms.Textarea(attrs={'cols':80})}
