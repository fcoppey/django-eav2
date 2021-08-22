from eav.models import EnumValue

def unspecified():
    try:
        return EnumValue.objects.get(value='unspecified')
    except:
        return EnumValue.objects.create(
            value='unspecified'
        )