# -----------------------------------------------------------------------------
# System Imports
# -----------------------------------------------------------------------------

from operator import itemgetter

# -----------------------------------------------------------------------------
# Public Imports
# -----------------------------------------------------------------------------

from netcad.design_services import Design
from netcad.topology import TopologyDesignService
from netcad.device import DeviceCatalog

# -----------------------------------------------------------------------------
# Private Imports
# -----------------------------------------------------------------------------

from .device_roles import MS220p8, MR52, MX65, MR42
from .profiles import AccessVlan1


def create_design(design: Design) -> Design:

    aliases = design.config["alias"] = dict()

    aliases["sw01"] = MS220p8(name="ms01-dl1")
    aliases["sw02"] = MS220p8(name="ms01-dl2")
    aliases["sw03"] = MS220p8(name="ms01-dl3")

    aliases["ap01"] = MR52("ap01-dl1")
    aliases["ap02"] = MR42("ap01-dl2")
    aliases["ap03"] = MR52("ap01-dl3")

    aliases["mx01"] = MX65(name="mx01-dl1")
    aliases["mx02"] = MX65(name="mx01-dl2")

    all_devs = list(aliases.values())

    design.add_devices(*all_devs)

    design.add_services(
        TopologyDesignService(topology_name=design.name, devices=all_devs)
    )

    cable_devices(design)

    design.update()
    return design


def cable_devices(design: Design):

    aliasses: DeviceCatalog = design.config["alias"]

    sw01, sw02, sw03 = itemgetter("sw01", "sw02", "sw03")(aliasses)
    ap01, ap02, ap03 = itemgetter("ap01", "ap02", "ap03")(aliasses)
    mx01, mx02 = itemgetter("mx01", "mx02")(aliasses)

    cable_id = 1

    # -------------------------------------------------------------------------
    # Cable Access-Points to Switches
    # -------------------------------------------------------------------------

    # ap01.0 --- sw03.1
    with ap01.interfaces["wired0"] as ap_w0, sw03.interfaces["1"] as sw03_1:
        ap_w0.profile = AccessVlan1()
        sw03_1.profile = AccessVlan1()
        ap_w0.cable_id = sw03_1.cable_id = f"cable_{cable_id}"
        cable_id += 1

    # ap02.0 --- sw01.2
    with ap02.interfaces["wired0"] as ap_w0, sw01.interfaces["2"] as sw_iface:
        ap_w0.profile = AccessVlan1()
        sw_iface.profile = AccessVlan1()
        ap_w0.cable_id = sw_iface.cable_id = f"cable_{cable_id}"
        cable_id += 1

    # ap03.0 -- sw02.2
    with ap03.interfaces["wired0"] as ap_w0, sw02.interfaces["2"] as sw_iface:
        ap_w0.profile = AccessVlan1()
        sw_iface.profile = AccessVlan1()
        ap_w0.cable_id = sw_iface.cable_id = f"cable_{cable_id}"
        cable_id += 1

    # -------------------------------------------------------------------------
    # Cable Switches to Appliance
    # -------------------------------------------------------------------------

    # sw01.1 -- mx-office (not in design yet)

    # sw02.1 -- mx02.3
    with sw02.interfaces["1"] as sw_iface, mx02.interfaces["3"] as mx_iface:
        mx_iface.profile = AccessVlan1()
        sw_iface.profile = AccessVlan1()
        mx_iface.cable_id = sw_iface.cable_id = f"cable_{cable_id}"
        cable_id += 1

    # sw03.2 -- mx01.3
    with sw03.interfaces["2"] as sw_iface, mx01.interfaces["3"] as mx_iface:
        mx_iface.profile = AccessVlan1()
        sw_iface.profile = AccessVlan1()
        mx_iface.cable_id = sw_iface.cable_id = f"cable_{cable_id}"
        cable_id += 1
