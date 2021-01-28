import requests
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from quickstart.forms import CurrencyForm
from quickstart.models import Currency
from quickstart.serializers import CurrencySerializer



def endpoint(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            new_form.save()
            return redirect('/')

    else:
        form = CurrencyForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)




class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permissions_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]









