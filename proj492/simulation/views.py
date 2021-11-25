from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    context = {}
    return render(request, "simulation/index.html", context)
    # return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
