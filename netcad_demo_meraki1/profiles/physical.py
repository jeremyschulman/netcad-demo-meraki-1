from netcad.phy_port import (
    PhyPortProfile,
    PortCable,
    PhyPortSpeeds,
    CableMediaType,
    CableTerminationType,
    PortTransceiver,
    TranscieverFormFactorType,
    PhyPortTypes,
    PhyPortReachType,
)


__all__ = ["port_UTP_1G", "port_SFP_1G_T"]


port_UTP_1G = PhyPortProfile(
    name="UTP-1G",
    speed=PhyPortSpeeds.speed_1G,
    cabling=PortCable(media=CableMediaType.CAT6, termination=CableTerminationType.RJ45),
    transceiver=None,
)


port_SFP_1G_T = PhyPortProfile(
    name="SFP-1G-T",
    cabling=PortCable(media=CableMediaType.CAT6, termination=CableTerminationType.RJ45),
    speed=PhyPortSpeeds.speed_1G,
    transceiver=PortTransceiver(
        form_factor=TranscieverFormFactorType.RJ45,
        type=PhyPortTypes.type_1000BASE_T,
        reach=PhyPortReachType.short,
    ),
)
