from eav.models import EnumValue

def unspecified():
    return EnumValue.objects.get_or_create(value='unspecified')[0]
