from eav.models import EnumValue

def unspecified():
    return EnumValue.objects.get(value='unspecified')