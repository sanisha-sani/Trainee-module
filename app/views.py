from urllib import request
from django.shortcuts import render

# Create your views here.
def trainee_index(request):
    return render(request,'trainee_index.html')

def trainee_topic(request):
    return render(request, 'trainee_topic.html')

def trainee_currentTopic(request):
    return render(request, 'trainee_currentTopic.html')

def trainee_previousTopic(request):
    return render(request, 'trainee_previousTopic.html')

