from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home.html', context)

# We apply login_required() as a decorators to the topic() view function by prepending 
# login_required with @ symnol.
@login_required
def topics(request):
    """Shows all the topic."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    """Here in context dictionary we use keys value to access data."""
    return render(request, 'topics.html', context)


@login_required
def topic(request, topic_id):
    """Shows a singhle topic and all its enteries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.form
        form = TopicForm()
    else:
        # Post data submitted ; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('pages:topics')

    # Display a blank or invailid form
    context = {'form': form}
    return render(request, 'new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        """No data submmited; create a blank form."""
        form = EntryForm()
    else:
        # Post data submmited; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            # Here we are assigning the topic attribute of Entry mode = topic vairable
            new_entry.save()
            return redirect('pages:topic_name', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # Post data submmited; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:topic_name', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'edit_entry.html', context)
         