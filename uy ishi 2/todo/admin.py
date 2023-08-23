from django.contrib import admin

from .forms import ToDoForms
from .models import ToDoModel

class ToDoAdmin(admin.ModelAdmin):
    form = ToDoForms
    list_display = ('Task_name',)

admin.site.register(ToDoModel, ToDoAdmin)
