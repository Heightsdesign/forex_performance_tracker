from django.shortcuts import render
from .api import DataFetcher
from .forms import CurrencyForm
from .models import UserSettings
from .constants import time_frames
from trades.models import CurrencyPair
from users.models import User
import json


def homepage(request):
    return render(request, 'live/homepage.html')


def index(request):

    all_currency_pairs = CurrencyPair.objects.all()
    user = request.user
    # Gets the last user choice for live currency
    user_settings = UserSettings.objects.filter(user=user)[UserSettings.objects.count()-1]

    # Gets the id of the currency

    currency_choice = user_settings.currency_graph_id

    # Get the currency name from currency pair table
    currency_choice = CurrencyPair.objects.get(id=currency_choice).name
    time_frame = user_settings.time_frame
    print(type(User.objects.filter(email="phe@gmail.com")[0]))

    print(currency_choice)

    if currency_choice :
        if currency_choice[:-3] == "USD" and time_frame == "DAY":
            currency = DataFetcher(f"{currency_choice[-3:]}=X", "1d", "5m")
        elif currency_choice[:-3] == "USD" and time_frame == "WEEK":
            currency = DataFetcher(f"{currency_choice[-3:]}=X", "7d", "30m")
        elif currency_choice[:-3] == "USD" and time_frame == "MONTH":
            currency = DataFetcher(f"{currency_choice[-3:]}=X", "1mo", "2h")
        elif currency_choice[:-3] != "USD" and time_frame == "DAY":
            currency = DataFetcher(f"{currency_choice}=X", "1d", "5m")
        elif currency_choice[:-3] != "USD" and time_frame == "WEEK":
            currency = DataFetcher(f"{currency_choice}=X", "7d", "30m")
        elif currency_choice[:-3] != "USD" and time_frame == "MONTH":
            currency = DataFetcher(f"{currency_choice}=X", "1mo", "2d")
        else:
            currency = DataFetcher(f"{currency_choice}=X", "1d", "5m")
    else:
        currency_choice = "EURUSD"
        currency = DataFetcher("EURUSD=X", "1d", "5m")

    historicalData = currency.convert_ticker_to_line()
    real_time = currency.get_real_time_data()
    now = list(real_time.keys())[0]
    price = list(real_time.values())[0]
    historicalData[now] = price
    actualData = json.dumps(historicalData)
    form = CurrencyForm()

    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            currency_pair = CurrencyPair.objects.get(
                name=form.cleaned_data.get("currency_pair"),
            )
            time_frame = form.cleaned_data.get("time_frame")
            UserSettings.objects.create(
                user=user,
                currency_graph=currency_pair,
                time_frame=time_frame
            )

    context = {
        "actualData": actualData,
        "all_currency_pairs": all_currency_pairs,
        "form":form,
        "currency_choice":currency_choice,
        "time_frames":time_frames
    }

    return render(request, 'live/live_charts.html', context)

