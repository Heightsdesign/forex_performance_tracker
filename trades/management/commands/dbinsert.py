from django.core.management.base import BaseCommand, CommandError
from trades.models import CurrencyPair


class Command(BaseCommand):
    help = 'Insert data in a PostgreSQL database'

    def handle(self, *args, **options):

        currencies = [
            'EURUSD',
            'GBPUSD',
            'AUDUSD',
            'NZDUSD',
            'USDJPY',
            'USDCAD',
            'USDCHF',
            'USDRUB',
            'EURCHF',
            'EURGBP'
        ]

        for currency in currencies:
            CurrencyPair.objects.create(name=currency)
