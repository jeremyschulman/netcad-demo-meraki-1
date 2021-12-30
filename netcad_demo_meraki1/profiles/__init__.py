from netcad.device.l2_interfaces import InterfaceL2Access, InterfaceL2Trunk
from netcad.device import PeerInterfaceId

from netcad_demo_meraki1.vlans import vlan_native_1
from .physical import port_UTP_1G


class AccessVlan1(InterfaceL2Access):
    port_profile = port_UTP_1G
    vlan = vlan_native_1
    desc = PeerInterfaceId()
