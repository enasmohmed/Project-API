from django.forms import ModelForm
from django.utils import timezone

from quickstart.models import Currency


class CurrencyForm(ModelForm):

    class Meta:
        model = Currency
        fields = '__all__'
