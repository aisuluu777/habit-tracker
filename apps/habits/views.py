from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.utils.timezone import now
from datetime import timedelta
from .models import HabitModel, ProgressModel
from .serializers import HabitSerializer,  ProgressSerializer, ProgressHistorySerializer
from django.db.models import Count

class HabitListCreateView(ListCreateAPIView):
    queryset = HabitModel
    serializer_class = HabitSerializer


class HabitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = HabitModel
    serializer_class = HabitSerializer
    lookup_field = 'id'


class ProgressMark(CreateAPIView):
    queryset = ProgressModel
    serializer_class = ProgressSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        date = serializer.validated_data.get('date')
        habit_id = serializer.validated_data.get('habit_id')
        habit = ProgressModel.objects.filter(habit_id=habit_id, user=self.request.user)
        if date:
            ProgressModel.objects.filter(habit_id=habit, date=date).exists()
            return Response(data={'Object with this date already exists'}, status=HTTP_400_BAD_REQUEST)
        else:
            now = now.date
            progress = ProgressModel.objects.create(serializer.validated_data, date=now)
            return Response(data=self.serializer_class(progress), status=HTTP_201_CREATED)
        


class StatisticView(GenericAPIView):
    queryset = ProgressModel
    serializer_class = ProgressHistorySerializer

    def get(self, request):
        period = request.query_params.get('period')
        habit_id = request.query_params.get('habit_id')
        user = request.user
        today = now().date()
        if period == 'week':
            day = today.weekday()
            start = today - timedelta(days=day)
            end = start + timedelta(days=6)
        elif period == 'month':
            start = today.replace(day=1)
            next_month = start.replace(month=start.month + 1) if start < 12 else start.replace(year=start.year + 1, month=1)
            end = next_month - timedelta(days=1)
        else:
            total = ProgressModel.objects.filter(habit_id=habit_id).aaggregate(
                total=Count('id')
            )
            return Response(data=self.serializer_class(total), status=HTTP_200_OK)

        statistic = ProgressModel.objects.filter(
            habit_id=habit_id, 
            date__range=(start, end) ).aaggregate(completed_count=Count('id'))
        
        return Response({
                'period' : period,
                'start' : start.isoformat(),
                'end' : end.isoformat(),
                'completed_count' : statistic['completed_count']
            })


            

            



            

