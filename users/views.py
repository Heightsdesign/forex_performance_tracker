from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
import json
import datetime
from .models import User, Strategy
from trades.models import Trade, CurrencyPair
from .forms import TradeForm, UserCreationForm, LoginForm, StrategyForm
from trades.calculator import get_daily_trades, get_volumes


def user_page(request, user_id):

    user = User.objects.get(pk=user_id)

    if str(request.user) == user.email:

        all_trades = Trade.objects.filter(user__first_name=user.first_name)
        all_currency_pairs = CurrencyPair.objects.all()
        total_trades = 0
        daily_performances = json.dumps(get_daily_trades(user))
        volumes = json.dumps(get_volumes(user))
        positions = ["BUY", "SELL"]
        user_strategy = Strategy.objects.filter(user=user).last()

        today_min = datetime.datetime.combine(
            datetime.date.today(),
            datetime.time.min
        )
        today_max = datetime.datetime.combine(
            datetime.date.today(),
            datetime.time.max
        )

        if user_strategy is not None:
            user_strategy = user_strategy.content

        try:
            today_trades = Trade.objects.filter(
                user=user, datetime__range=(today_min, today_max)
            )

        except Trade.DoesNotExist:
            today_trades = None

        for trade in all_trades:
            total_trades += trade.profit

        strategy_form = StrategyForm()
        form = TradeForm()

        if request.method == "POST" and "stratButton" in request.POST:
            strategy_form = StrategyForm(request.POST)
            form = TradeForm()
            if strategy_form.is_valid():
                content = strategy_form.cleaned_data.get("content")

                Strategy.objects.create(user=user, content=content)

        elif request.method == "POST" and "tradeButton" in request.POST:
            form = TradeForm(request.POST)
            strategy_form = StrategyForm()
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

        context = {
            "user": user,
            "all_currency_pairs": all_currency_pairs,
            "total_trades": total_trades,
            "daily_performances": daily_performances,
            "strategy_form": strategy_form,
            "form": form,
            "positions": positions,
            "volumes": volumes,
            "today_trades": today_trades,
            "user_strategy": user_strategy,
        }

        return render(request, "users/user_page.html", context)

    elif str(request.user) != user.email:
        message = "NOT AUTHORIZED !"
        context = {"message": message}
        return render(request, "users/thank_you.html", context)


def sign_up(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            capital = form.cleaned_data.get("capital")

            user = User.objects.filter(email=email)

            if not user.exists():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=None,
                    last_name=None,
                    country=None,
                    city=None,
                    zip_code=None,
                    address=None,
                    capital=capital,
                    password=password,
                )

                message = f"{username} HAS BEEN SUCCESSFULLY REGISTERED !"
                success = True
                context = {"message": message, "success": success}

            else:
                message = f"{username} : ACCOUNT IS ALREADY REGISTERED !"
                context = {"message": message}

            return render(request, "users/thank_you.html", context)

    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "users/sign_up_page.html", context)


def login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, email=email, password=password)

            if user is not None and user.is_authenticated:
                auth_login(request, user)
                message = f"USER CONNECTED: {user.username}!"

            else:
                message = "WRONG EMAIL OR PASSWORD"

            context = {"message": message}
            return render(request, "users/thank_you.html", context)

        else:
            message = "WRONG EMAIL OR PASSWORD"

        context = {"message": message}
        return render(request, "users/thank_you.html", context)

    else:
        form = LoginForm()

    context = {"form": form}

    return render(request, "users/login_page.html", context)


def logout_view(request):

    logout(request)
    message = "Utilisateur d??connect??!"
    return redirect("/")


def performance(request, user_id):

    user = User.objects.get(pk=user_id)
    return render(request, "trades/performance.html")
