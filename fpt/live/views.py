from django.shortcuts import render

def homepage(request):
    return render(request, 'live/homepage.html')

def live_charts(request):
    return render(request, 'live/live_charts.html')
