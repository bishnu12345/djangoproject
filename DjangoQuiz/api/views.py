from django.shortcuts import render

#Create your views here.
from rest_framework import generics

from api.Serializer import QuestionSerializer
from quiz.models import Question


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

