from users.forms import get_choices
from django import forms
from django.forms.widgets import TextInput
from trades.models import CurrencyPair
from .constants import time_frames


class CurrencyForm(forms.Form):

    currency_pair = forms.CharField(
        label="currency_pair",
        max_length=6,
        required=True,
        widget=forms.Select(choices=get_choices(CurrencyPair)),
    )

    time_frame = forms.CharField(
        label="time_frame",
        max_length=6,
        required=True,
        widget=forms.Select(choices=time_frames),
    )
