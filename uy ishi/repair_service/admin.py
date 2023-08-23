from django.contrib import admin
from .models import UstaModel, OrderModel
from .forms import OrderForms, UstaForms


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    form = OrderForms
    list_display = ('buzilish_sababi', 'client_name')


class UstaAdmin(admin.ModelAdmin):
    form = UstaForms
    list_display = ('name', 'mutaxasislig')


admin.site.register(UstaModel, UstaAdmin)
admin.site.register(OrderModel, OrderAdmin)
