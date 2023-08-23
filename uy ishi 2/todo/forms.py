from django import forms
from .models import ToDoModel

class ToDoForms(forms.ModelForm):
    Task_name_uz = forms.CharField()
    Task_name_en = forms.CharField(required=False)
    Task_name_ru = forms.CharField(required=False)