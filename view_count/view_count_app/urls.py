from django.urls import path
from . import views

urlpatterns = [
    path("", views.increment_count),
    ]