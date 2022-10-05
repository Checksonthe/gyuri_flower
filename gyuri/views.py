#from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'gyuri/question_list.html', context)