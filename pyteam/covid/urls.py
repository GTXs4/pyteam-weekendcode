from django.urls import path
from . import views

urlpatterns = [
    path("covid/", views.HomeView.as_view(), name="covid"),
]