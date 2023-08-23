from rest_framework import serializers
from .models import OrderModel, UstaModel


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ("id", "client_name", "buzilish_sababi",  "added_at", "updated_at", "usta_id")


class UstaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UstaModel
        fields = '__all__'