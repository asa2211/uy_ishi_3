from modeltranslation.translator import translator, TranslationOptions
from todo.models import ToDoModel


class ToDoTranslationOptions(TranslationOptions):
    fields = ('Task_name',)


translator.register(ToDoModel, ToDoTranslationOptions)
