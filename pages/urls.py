"""Defined urls patterns for learing logs."""
from django.urls import path
from . import views



app_name = 'pages'

urlpatterns = [
    # Home page
    path('', views.home_page, name='home'),
    # Page that shows all the topics.
    path('topics/', views.topics, name='topics'),
    # Detai page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic_name'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry.format
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for the editing a new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]

