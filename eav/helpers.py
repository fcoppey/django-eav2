from eav.models import EnumValue

def unspecified():
    try:
        unspecified = EnumValue.objects.get(value='unspecified')
    except:
        unspecified = EnumValue.objects.create(
            value='unspecified'
        )

    return unspecified