from django.shortcuts import render
from .models import User
from trades.calculator import percentage_calculator
from trades.models import Trade

# Create your views here.
def user_page(request, user_id):

    user = User.objects.get(pk=user_id)
    all_trades = Trade.objects.filter(user__first_name=user.first_name)

    total_trades = 0
    for trade in all_trades:
        total_trades += trade.profit

    context = {"user": user, "total_trades": total_trades}

    return render(request, 'users/user_page.html', context)

def sign_up(request):
    return render(request, 'users/sign_up_page.html')

def login(request):
    return render(request, 'users/login_page.html')
