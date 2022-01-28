from django import forms
from django.forms.widgets import TextInput

class TradeForm(forms.Form):

    currrency_pair = forms.CharField(
        label="currency_pair",
        max_length=6,
        widget=TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    entry_point = forms.DecimalField(
        label="entry_point",
        max_digits=8,
        decimal_places=5,
        required=True,
    )

    exit_point = forms.DecimalField(
        label="exit_point",
        max_digits=8,
        decimal_places=5,
        required=True,
    )

    profit = forms.DecimalField(
        label="profit",
        max_digits=10,
        decimal_places=2,
        required=True,
    )
