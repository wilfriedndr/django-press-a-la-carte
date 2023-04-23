from django.db import models
from django.utils import timezone


class Pdf(models.Model):
    """
    Create an abstract model for new files
    """
    name = models.CharField(max_length="50", null=False)
    path = models.CharField(max_length="250", null=False)
    created_at = models.DateTimeField(default=timezone.now)


class NewFile(models.Model):
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    pdf = models.ForeignKey(PDF, on_delete=models.CASCADE)


class Subscriber(models.Model):
    age = models.PositiveIntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class Rubric(models.Model):
    type = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)


class User(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_permissions = models.CharField(max_length=255)


class Advertising(models.Model):
    type = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)


class Category(models.Model):
    SPORT = 'Sport'
    CINEMA = 'Cinema'
    CATEGORY_CHOICES = [
        (SPORT, 'Sport'),
        (CINEMA, 'Cinema'),
    ]
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
