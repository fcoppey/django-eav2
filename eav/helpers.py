from eav.models import EnumValue

def unspecified():
    try:
        return EnumValue.objects.get(value='unspecified')
    except:
        return EnumValue.objects.create(
            value='unspecified',
            value_display='Unspecified',
            value_display_fr='Non spécifié'
        )