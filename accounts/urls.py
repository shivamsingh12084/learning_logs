"""Defines URL patterns for users"""

from django.urls import path, include

from .views import SignupPageView

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    # Registration page.
    path('signup/', SignupPageView.as_view(), name='signup'),
]