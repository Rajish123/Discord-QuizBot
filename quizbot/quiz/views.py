from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question
from .serializers import RandomQuestionSerializer
from rest_framework.response import Response


class RandomQuestion(APIView):

    def get(self,request,format = None, **kwargs):
        # selecting all the questions and ordering randomly and selection top answer one at a time
        question = Question.objects.filter().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many = True)
        return Response(serializer.data)

