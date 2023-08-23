from django import forms
from .models import OrderModel, UstaModel


class OrderForms(forms.ModelForm):
    buzilish_sababi_uz = forms.CharField()
    buzilish_sababi_en = forms.CharField(required=False)
    buzilish_sababi_ru = forms.CharField(required=False)
    client_name_uz = forms.CharField()
    client_name_en = forms.CharField(required=False)
    client_name_ru = forms.CharField(required=False)


class Meta:
    model = OrderModel
    exclude = ['buzilish_sababi', 'client_name']


class UstaForms(forms.ModelForm):
    mutaxasislig_uz = forms.CharField()
    mutaxasislig_en = forms.CharField(required=False)
    mutaxasislig_ru = forms.CharField(required=False)


class Meta:
    model = UstaModel
    exclude = ['mutaxasislig']
