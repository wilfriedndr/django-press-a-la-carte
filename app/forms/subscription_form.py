from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class SubscriberForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'address', 'age']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        fields = ['rubrics']