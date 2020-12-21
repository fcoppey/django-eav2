from modeltranslation.translator import translator, TranslationOptions

from .models import Attribute, EnumValue


class AttributeTranslationOptions(TranslationOptions):
    fields = ['name']


class EnumValueTranslationOptions(TranslationOptions):
    fields = ['value_display']


translator.register(Attribute, AttributeTranslationOptions)

translator.register(EnumValue, EnumValueTranslationOptions)
