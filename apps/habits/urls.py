from django.urls import path
from .views import HabitDetailView, HabitListCreateView, HabitCompleteMark

urlpatterns =  [
    path('habits/', HabitListCreateView.as_view()),
    path('habit/<int:id>/', HabitDetailView.as_view()),
    path('habit/mark', HabitCompleteMark.as_view())
]