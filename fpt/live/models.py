from django.db import models
from users.models import User
from trades.models import CurrencyPair
# Create your models here.


class UserSettings(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    currency_graph = models.ForeignKey(CurrencyPair, null=True, on_delete=models.SET_NULL)
    time_frame = models.CharField(max_length=5, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)