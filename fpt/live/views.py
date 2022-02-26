from django.shortcuts import render
from .api import DataFetcher
import time
import json


def homepage(request):
    return render(request, 'live/homepage.html')


def index(request):
        return render(request, 'live/live_charts.html')

