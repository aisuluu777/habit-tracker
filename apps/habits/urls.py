from django.urls import path
from .views import HabitDetailView, HabitListCreateView

urlpatterns =  [
    path('habits/', HabitListCreateView.as_view()),
    path('habit/<int:id>/', HabitDetailView.as_view())
]