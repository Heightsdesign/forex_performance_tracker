from django import forms
from django.forms.widgets import TextInput
from trades.models import CurrencyPair
from .models import Country, City


def get_choices(db_obj):

    objs = db_obj.objects.all()
    choices = []

    for obj in objs:
        choices.append(obj.name)

    return choices


class TradeForm(forms.Form):

    currency_pair = forms.CharField(
        label="currency_pair",
        max_length=6,
        required=True,
        widget=forms.Select(choices=get_choices(CurrencyPair)),
    )

    position = forms.CharField(
        label="currency_pair",
        max_length=4,
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


class UserCreationForm(forms.Form):

    username = forms.CharField(
        label="username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username_input_sub",
                "placeholder": "Username",
            }
        ),
        max_length=30,
        required=True,
    )

    email = forms.EmailField(
        label="email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email_input_sub",
                "placeholder": "Email",
            }
        ),
        max_length=50,
        required=True,
    )

    capital = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )

    password = forms.CharField(
        label="password",
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "id": "password_input_sub",
                "placeholder": "Password",
            }
        ),
        required=True,
    )


class LoginForm(forms.Form):

    email = forms.EmailField(
        label="email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "email_input_log",
                "placeholder": "email",
            }
        ),
        max_length=50,
        required=True,
    )

    password = forms.CharField(
        label="password",
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "password",
                "id": "password_input_log",
                "placeholder": "Password",
            }
        ),
        required=True,
    )


class UserInfoForm(forms.Form):

    first_name = forms.CharField(
        label="first_name",
        widget=forms.TextInput(
            attrs={
                "id": "first_name",
                "placeholder": "First name",
            }
        ),
        max_length=30,
    )
    last_name = forms.CharField(
        label="last_name",
        widget=forms.TextInput(
            attrs={
                "id": "last_name",
                "placeholder": "Last name",
            }
        ),
        max_length=30,
    )

    country = forms.CharField(
        label="country",
        max_length=30,
        required=True,
        widget=forms.Select(choices=get_choices(Country)),
    )

    city = forms.CharField(
        label="city",
        max_length=30,
        required=True,
        widget=forms.Select(choices=get_choices(City)),
    )

    zip_code = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "id": "zip_code",
                "placeholder": "Zip",
            }
        )
    )

    address = forms.CharField(
        label="address",
        widget=forms.TextInput(
            attrs={
                "id": "address",
                "placeholder": "Address",
            }
        ),
        max_length=200,
    )


class StrategyForm(forms.Form):

    content = forms.CharField(
        label="content",
        widget=forms.Textarea,
        max_length=300
    )
