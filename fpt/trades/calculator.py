from django.utils import timezone
import datetime
from users.models import User
from .models import Trade, CurrencyPair


def percentage_calculator(total_val, partial_val):

    percentage = 0

    if total_val > partial_val and partial_val > 0:

        percentage = 100 * partial_val / total_val

    elif partial_val < 0:
        partial_val = -partial_val
        percentage = 100 * partial_val / total_val
        percentage = -percentage

    elif partial_val == 0:
        print("No data")

    else:
        print("ERROR: Total value inferior to partial value")

    return percentage


print(percentage_calculator(12500, 100))


def get_daily_trades(user):

    day_index = 0
    daily_performances = {}
    capital = user.capital

    print(f"Capital = {capital}")

    used_trades = []

    for i in range(30):
        day_index += 1
        date = timezone.now() - datetime.timedelta(days=day_index)

        daily_trades = Trade.objects.filter(
            user__id=user.id,
            datetime__gt=date
        )

        daily_profit = 0

        for trade in daily_trades:
            if trade not in used_trades:
                used_trades.append(trade)
                daily_profit += trade.profit
                print(f"date : {trade.datetime} / profit : {trade.profit}")

        # daily_performance = {day_index: float(percentage_calculator(capital, daily_profit))}
        # daily_performances.append(daily_performance)

        daily_performances[day_index] = float(percentage_calculator(capital, daily_profit))

    return daily_performances


def get_volumes(user):

    currencies = CurrencyPair.objects.all()
    total_trades = len(Trade.objects.filter(user__id=user.id))
    number_trades = 0
    volumes = {}

    for currency in currencies:
        data = Trade.objects.filter(
            user__id=user.id,
            currency_pair=currency,
        )

        number_trades = len(data)
        volumes[currency.name] = float(percentage_calculator(total_trades, number_trades))

    return volumes






