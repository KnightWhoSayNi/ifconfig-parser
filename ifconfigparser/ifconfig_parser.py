#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: ifconfig_parser
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:03
#    Python Version: 3.6
#
# ======================================================
import re
from collections import namedtuple


class IfconfigParser(object):
    attributes = ['name', 'type', 'mac_addr', 'ipv4_addr', 'ipv4_bcast', 'ipv4_mask', 'ipv6_addr', 'ipv6_mask',
                  'ipv6_scope', 'state', 'mtu', 'metric', 'rx_packets', 'rx_errors', 'rx_dropped', 'rx_overruns',
                  'rx_frame', 'tx_packets', 'tx_errors', 'tx_dropped', 'tx_overruns', 'tx_carrier', 'tx_collisions']

    def __init__(self, console_output):
        """
        :param console_output:
        """

        if isinstance(console_output, list):
            source_data = " ".join(console_output)
        else:
            source_data = console_output.replace("\n", " ")
        self.interfaces = self.parser(source_data=source_data)

    def list_interfaces(self):
        """

        :return:
        """
        return sorted(self.interfaces.keys())

    def count_interfaces(self):
        """

        :return:
        """
        return len(self.interfaces.keys())

    def filter_interfaces(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        for attr in kwargs.keys():
            if attr not in IfconfigParser.attributes:
                raise ValueError("Attribute [{}] not supported.".format(attr))

        filtered_interfaces = []
        for name, details in self.interfaces.items():

            if all(getattr(details, attr) == kwargs[attr] for attr in kwargs.keys()):
                filtered_interfaces.append(name)

        return sorted(filtered_interfaces)

    def get_interface(self, name):
        """

        :param name:
        :return:
        """
        if name in self.list_interfaces():
            return self.interfaces[name]
        else:
            raise InterfaceNotFound("Interface [{}] not found.".format(name))

    def get_interfaces(self):
        """

        :return:
        """
        return self.interfaces

    def is_available(self, name):
        """

        :param name:
        :return:
        """
        return name in self.interfaces

    def parser(self, source_data):
        """

        :param source_data:
        :return:
        """

        # Linux syntax
        re_linux_interface = re.compile(
            r"(?P<name>[a-zA-Z0-9:._-]+)\s+Link encap:(?P<type>\S+\s?\S+)(\s+HWaddr\s+\b"
            r"(?P<mac_addr>[0-9A-Fa-f:?]+))?",
            re.I)
        re_linux_ipv4 = re.compile(
            r"inet addr:(?P<ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})(\s+Bcast:"
            r"(?P<ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3}))?\s+Mask:(?P<ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})",
            re.I)
        re_linux_ipv6 = re.compile(
            r"inet6 addr:\s+(?P<ipv6_addr>\S+)/(?P<ipv6_mask>[0-9]+)\s+Scope:(?P<ipv6_scope>Link|Host)",
            re.I)
        re_linux_state = re.compile(
            r"(?P<state>.*)\s+MTU:(?P<mtu>[0-9]+)\s+Metric:(?P<metric>[0-9]+)", re.I)
        re_linux_rx = re.compile(
            r"RX packets:(?P<rx_packets>[0-9]+)\s+errors:(?P<rx_errors>[0-9]+)\s+dropped:"
            r"(?P<rx_dropped>[0-9]+)\s+overruns:(?P<rx_overruns>[0-9]+)\s+frame:(?P<rx_frame>[0-9]+)",
            re.I)
        re_linux_tx = re.compile(
            r"TX packets:(?P<tx_packets>[0-9]+)\s+errors:(?P<tx_errors>[0-9]+)\s+dropped:"
            r"(?P<tx_dropped>[0-9]+)\s+overruns:(?P<tx_overruns>[0-9]+)\s+carrier:(?P<tx_carrier>[0-9]+)",
            re.I)
        re_linux_tx_stats = re.compile(r"collisions:(?P<tx_collisions>[0-9]+)\s+txqueuelen:[0-9]+", re.I)
        re_linux = [re_linux_interface, re_linux_ipv4, re_linux_ipv6, re_linux_state, re_linux_rx, re_linux_tx,
                    re_linux_tx_stats]

        # OpenBSD syntax
        re_openbsd_interface = re.compile(
            r"(?P<name>[a-zA-Z0-9:._-]+):\s+flags=(?P<flags>[0-9]+)<(?P<state>\S+)>\s+mtu\s+(?P<mtu>[0-9]+)",
            re.I)
        re_openbsd_ipv4 = re.compile(
            r"inet (?P<ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+netmask\s+"
            r"(?P<ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})(\s+broadcast\s+"
            r"(?P<ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3}))?",
            re.I)
        re_openbsd_ipv6 = re.compile(
            r"inet6\s+(?P<ipv6_addr>\S+)\s+prefixlen\s+(?P<ipv6_mask>[0-9]+)\s+scopeid\s+[0-9]+x[0-9]+<"
            r"(?P<ipv6_scope>link|host)>",
            re.I)
        re_openbsd_details = re.compile(
            r"\S+\s+(?:(?P<mac_addr>[0-9A-Fa-f:?]+)\s+)?txqueuelen\s+[0-9]+\s+\((?P<type>\S+\s?\S+)\)", re.I)
        re_openbsd_rx = re.compile(r"RX packets (?P<rx_packets>[0-9]+)\s+bytes.*", re.I)
        re_openbsd_rx_stats = re.compile(
            r"RX errors (?P<rx_errors>[0-9]+)\s+dropped\s+(?P<rx_dropped>[0-9]+)\s+overruns\s+"
            r"(?P<rx_overruns>[0-9]+)\s+frame\s+(?P<rx_frame>[0-9]+)",
            re.I)
        re_openbsd_tx = re.compile(r"TX packets (?P<tx_packets>[0-9]+)\s+bytes.*", re.I)
        re_openbsd_tx_stats = re.compile(
            r"TX errors (?P<tx_errors>[0-9]+)\s+dropped\s+(?P<tx_dropped>[0-9]+)\s+overruns\s+"
            r"(?P<tx_overruns>[0-9]+)\s+carrier\s+(?P<tx_carrier>[0-9]+)\s+collisions\s+(?P<tx_collisions>[0-9]+)",
            re.I)
        re_openbsd = [re_openbsd_interface, re_openbsd_ipv4, re_openbsd_ipv6, re_openbsd_details, re_openbsd_rx,
                      re_openbsd_rx_stats, re_openbsd_tx, re_openbsd_tx_stats]

        # FreeBSD syntax
        # TODO: cover all interface attributes
        re_freebsd_interface = re.compile(
            r"(?P<name>[a-zA-Z0-9:._-]+):\s+flags=(?P<flags>[0-9]+)<(?P<state>\S+)>\s+metric\s+"
            r"(?P<metric>[0-9]+)\s+mtu\s+(?P<mtu>[0-9]+)",
            re.I)
        re_freebsd_ipv4 = re.compile(
            r"inet (?P<ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+netmask\s+(?P<ipv4_mask>0x\S+)(\s+broadcast\s+"
            r"(?P<ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3}))?",
            re.I)
        re_freebsd_details = re.compile(r"ether\s+(?P<mac_addr>[0-9A-Fa-f:?]+)", re.I)
        re_freebsd = [re_freebsd_interface, re_freebsd_ipv4, re_freebsd_details]

        available_interfaces = dict()

        for pattern in [re_linux_interface, re_openbsd_interface, re_freebsd_interface]:
            network_interfaces = re.finditer(pattern, source_data)
            positions = []
            while True:
                try:
                    pos = next(network_interfaces)
                    positions.append(max(pos.start() - 1, 0))
                except StopIteration:
                    break
            if positions:
                positions.append(len(source_data))
                break

        if not positions:
            return available_interfaces

        for l, r in zip(positions, positions[1:]):
            chunk = source_data[l:r]
            _interface = dict()
            for pattern in re_linux + re_openbsd + re_freebsd:
                match = re.search(pattern, chunk)
                if match:
                    details = match.groupdict()
                    _interface.update(details)
            if _interface is not None:
                available_interfaces[_interface['name']] = self.update_interface_details(_interface)

        return available_interfaces

    @staticmethod
    def update_interface_details(interface):
        for attr in IfconfigParser.attributes:
            if attr not in interface:
                interface[attr] = None
        return namedtuple('Interface', interface.keys())(**interface)


class InterfaceNotFound(Exception):
    """
    """
    pass
