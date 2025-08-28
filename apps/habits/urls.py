from django.urls import path
from .views import HabitDetailView, HabitListCreateView, ProgressMark, StatisticView

urlpatterns =  [
    path('habits/', HabitListCreateView.as_view()),
    path('habit/<int:id>/', HabitDetailView.as_view()),
    path('habit/mark/', ProgressMark.as_view()),
    path('staistic/', StatisticView.as_view())
]