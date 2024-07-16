from modeltranslation.translator import translator, TranslationOptions
from .models import User

class UserTranslationOptions(TranslationOptions):
    fields = ('username', 'name')

translator.register(User, UserTranslationOptions)
