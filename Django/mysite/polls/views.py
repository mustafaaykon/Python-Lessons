from django.shortcuts import render
from django.http import HttpResponse

#   http://127.0.0.1:8000/polls/index


def index(request):
    return HttpResponse("Hello Index, world. You're at the polls index.")


#   http://127.0.0.1:8000/polls/about
def about(request):
    return HttpResponse("Hello About, world. You're at the polls index.")
