# allows application to get data from database and convert it into format so that other applications can understand and utilize

from dataclasses import field
from rest_framework import serializers
from .models import Question,Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many = True, read_only = True)

    class Meta:
        model = Question
        fields = [
            'title',
            'answer',
        ]
