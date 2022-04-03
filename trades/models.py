from users.models import User
from django.db import models

# Create your models here.


class CurrencyPair(models.Model):

    name = models.CharField(max_length=6, blank=True)


class Trade(models.Model):

    user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE
    )

    currency_pair = models.ForeignKey(
        CurrencyPair,
        null=True,
        on_delete=models.CASCADE
    )

    position = models.CharField(max_length=4, blank=True)

    entry_point = models.DecimalField(max_digits=8, decimal_places=5)

    exit_point = models.DecimalField(max_digits=8, decimal_places=5)

    diff = models.DecimalField(max_digits=8, decimal_places=5)

    profit = models.DecimalField(max_digits=10, decimal_places=2)

    datetime = models.DateTimeField(auto_now=True)
