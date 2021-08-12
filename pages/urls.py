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

]

