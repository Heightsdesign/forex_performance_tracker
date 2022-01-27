from django.shortcuts import render

# Create your views here.
def user_page(request):
    return render(request, 'users/user_page.html')

def sign_up(request):
    return render(request, 'users/sign_up_page.html')

def login(request):
    return render(request, 'users/login_page.html')
