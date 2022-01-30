from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from trades.calculator import percentage_calculator
from trades.models import Trade, CurrencyPair
from .forms import TradeForm


def user_page(request, user_id):

    user = User.objects.get(pk=user_id)
    all_trades = Trade.objects.filter(user__first_name=user.first_name)
    all_currency_pairs = CurrencyPair.objects.all()
    total_trades = 0
    for trade in all_trades:
        total_trades += trade.profit

    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            # Creates a currency pair instance
            currency_pair = CurrencyPair.objects.get(
                name=form.cleaned_data.get("currency_pair"),
            )
            entry_point = form.cleaned_data.get("entry_point")
            exit_point = form.cleaned_data.get("exit_point")
            diff = entry_point - exit_point

            Trade.objects.create(
                user=user,
                currency_pair=currency_pair,
                position=form.cleaned_data.get("position"),
                entry_point=entry_point,
                exit_point=exit_point,
                diff=diff,
                profit=form.cleaned_data.get("profit"),
            )

    else:
        form = TradeForm()

    context = {
        "user": user,
        "all_currency_pairs": all_currency_pairs,
        "total_trades": total_trades,
        "form": form
    }

    return render(request, 'users/user_page.html', context)


def sign_up(request):

    return render(request, 'users/sign_up_page.html')


def login(request):

    return render(request, 'users/login_page.html')
