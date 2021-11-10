from eav.models import EnumValue

def unspecified():
    try:
        unspecified = EnumValue.objects.get(value='unspecified')
    except:
        unspecified = EnumValue.objects.create(
            value='unspecified'
        )

    return unspecified


def direct_measurement():
    try:
        direct = EnumValue.objects.get(value='direct_contact')
    except:
        direct = EnumValue.objects.create(
            value='direct_contact'
        )

    return direct


def homogenized_powder():
    try:
        homogenized_powder = EnumValue.objects.get(value='powder')
    except:
        homogenized_powder = EnumValue.objects.create(
            value='powder'
        )

    return homogenized_powder