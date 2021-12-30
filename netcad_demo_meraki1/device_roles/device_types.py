from netcad.device import Device

__all__ = ["MS220p8", "MX65", "MR52"]


class Meraki(Device):
    """Any Meraki device"""

    os_name = "meraki"


class MS220p8(Meraki):
    product_model = "MS220-8P"


class MerakiMX(Meraki):
    def __init__(self, *vargs, **kwargs):
        super().__init__(*vargs, **kwargs)
        for if_name, if_obj in self.interfaces.items():
            if if_name.isdigit():
                if (if_port := int(if_name)) >= 3:
                    if_obj.cable_port_id = if_port - 3


class MX65(MerakiMX):
    product_model = "MX65"


class MerakiAP(Meraki):
    is_wireless = True

    def __init__(self, *vargs, **kwargs):
        super().__init__(*vargs, **kwargs)
        self.interfaces["wired0"].cable_port_id = "0"


class MR52(MerakiAP):
    product_model = "MR52"


class MR42(MerakiAP):
    product_model = "MR42"
