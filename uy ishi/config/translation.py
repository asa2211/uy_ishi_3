from modeltranslation.translator import translator, TranslationOptions
from repair_service.models import OrderModel, UstaModel


class OrdersTranslationOptions(TranslationOptions):
    fields = ('buzilish_sababi', 'client_name')


class UstaTranslationOptions(TranslationOptions):
    fields = ('mutaxasislig',)


translator.register(OrderModel, OrdersTranslationOptions)
translator.register(UstaModel, UstaTranslationOptions)
