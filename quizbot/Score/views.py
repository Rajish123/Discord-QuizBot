from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ScoreSerializer
from .models import Score
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F


class UpdateScores(APIView):
    def post(self,request,format = None):
        # collect data from bot i.e, from request
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            points = serializer.validated_data['points']

            if Score.objects.filter(name = name).exists():
                serializer = Score.objects.get(name = name)
                # F is special django feature that allows us to access point field
                serializer.points = F('points') + points
            serializer.save()
            return Response(None, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

