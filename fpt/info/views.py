from django.shortcuts import render

# Create your views here.

def about_us(request):
    return render(request, 'info/about_us.html')

def legal(request):
    return render(request, 'info/legal.html')
