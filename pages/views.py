from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Topic

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home.html', context)

def topics(request):
    """Shows all the topic."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    """Here in context dictionary we use keys value to access data."""
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """Shows a singhle topic and all its enteries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)