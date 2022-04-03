from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Country(models.Model):
    name = models.CharField(max_length=60)


class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)


class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        email,
        first_name,
        last_name,
        country,
        city,
        zip_code,
        address,
        capital,
        password=None,
    ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            country=country,
            city=city,
            zip_code=zip_code,
            address=address,
            capital=capital,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    objects = UserManager()
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    zip_code = models.IntegerField(
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    capital = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True


class Strategy(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=300, blank=True, null=True)


class DailyProfit(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now=True)
