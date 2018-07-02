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
            source_data = console_output
        else:
            source_data = console_output.splitlines()
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

    @staticmethod
    def parser(source_data):
        """

		:param source_data:
		:return:
		"""

        # Linux syntax
        re_linux_interface = re.compile(
            r"(?P<name>[a-zA-Z0-9:._-]+)\s+Link encap\:(?P<type>\S+\s?\S+)(\s+HWaddr\s+\b(?P<mac_addr>[0-9A-Fa-f:?]+))?",
            re.I)
        re_linux_ipv4 = re.compile(
            r"inet addr:(?P<ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})(\s+Bcast:(?P<ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3}))?\s+Mask:(?P<ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})",
            re.I)
        re_linux_ipv6 = re.compile(
            r"inet6 addr:\s+(?P<ipv6_addr>\S+)\/(?P<ipv6_mask>[0-9]+)\s+Scope:(?P<ipv6_scope>Link|Host)",
            re.I)
        re_linux_state = re.compile(
            r"(?P<state>.*)\s+MTU:(?P<mtu>[0-9]+)\s+Metric:(?P<metric>[0-9]+)", re.I)
        re_linux_rx = re.compile(
            r"RX packets:(?P<rx_packets>[0-9]+)\s+errors:(?P<rx_errors>[0-9]+)\s+dropped:(?P<rx_dropped>[0-9]+)\s+overruns:(?P<rx_overruns>[0-9]+)\s+frame:(?P<rx_frame>[0-9]+)",
            re.I)
        re_linux_tx = re.compile(
            r"TX packets:(?P<tx_packets>[0-9]+)\s+errors:(?P<tx_errors>[0-9]+)\s+dropped:(?P<tx_dropped>[0-9]+)\s+overruns:(?P<tx_overruns>[0-9]+)\s+carrier:(?P<tx_carrier>[0-9]+)",
            re.I)
        re_linux_tx_stats = re.compile(r"collisions:(?P<tx_collisions>[0-9]+)\s+txqueuelen:[0-9]+", re.I)
        re_linux = [re_linux_ipv4, re_linux_ipv6, re_linux_state, re_linux_rx, re_linux_tx, re_linux_tx_stats]

        # OpenBSD syntax
        re_openbsd_interface = re.compile(
            r"(?P<name>[a-zA-Z0-9:._-]+):\s+flags=(?P<flags>[0-9]+)<(?P<state>\S+)>\s+mtu\s+(?P<mtu>[0-9]+)",
            re.I)
        re_openbsd_ipv4 = re.compile(
            r"inet (?P<ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+netmask\s+(?P<ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+broadcast\s+(?P<ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3})",
            re.I)
        re_openbsd_ipv6 = re.compile(
            r"inet6\s+(?P<ipv6_addr>\S+)\s+prefixlen\s+(?P<ipv6_mask>[0-9]+)\s+scopeid\s+[0-9]+x[0-9]+<(?P<ipv6_scope>link)>",
            re.I)
        re_openbsd_details = re.compile(
            r"\S+\s+(?P<mac_addr>[0-9A-Fa-f:?]+)\s+txqueuelen\s+[0-9]+\s+\((?P<type>\S+)\)", re.I)
        re_openbsd_rx = re.compile(r"RX packets (?P<rx_packets>[0-9]+)\s+bytes.*", re.I)
        re_openbsd_rx_stats = re.compile(
            r"RX errors (?P<rx_errors>[0-9]+)\s+dropped\s+(?P<rx_dropped>[0-9]+)\s+overruns\s+(?P<rx_overruns>[0-9]+)\s+frame\s+(?P<rx_frame>[0-9]+)",
            re.I)
        re_openbsd_tx = re.compile(r"TX packets (?P<tx_packets>[0-9]+)\s+bytes.*", re.I)
        re_openbsd_tx_stats = re.compile(
            r"TX errors (?P<tx_errors>[0-9]+)\s+dropped\s+(?P<tx_dropped>[0-9]+)\s+overruns\s+(?P<tx_overruns>[0-9]+)\s+carrier\s+(?P<tx_carrier>[0-9]+)\s+collisions\s+(?P<tx_collisions>[0-9]+)",
            re.I)
        re_openbsd = [re_openbsd_interface, re_openbsd_ipv4, re_openbsd_ipv6, re_openbsd_details, re_openbsd_rx,
                      re_openbsd_rx_stats, re_openbsd_tx, re_openbsd_tx_stats]

        # FreeBSD syntax
        # TODO: Add regular expressions

        available_interfaces = dict()

        _interface_found = False
        _interface = None
        _regex_list = None

        lines = len(source_data)
        for index, line in enumerate(source_data):
            line = line.strip()
            if not _interface_found:
                m_linux = re.match(re_linux_interface, line)
                if m_linux:
                    _interface_found = True
                    _regex_list = re_linux
                    _interface = m_linux.groupdict()
                    continue
                m_openbsd = re.match(re_openbsd_interface, line)
                if m_openbsd:
                    _interface_found = True
                    _regex_list = re_openbsd
                    _interface = m_openbsd.groupdict()
                    continue
            else:
                if line == '' or index == (lines - 1):

                    for attr in IfconfigParser.attributes:
                        if attr not in _interface:
                            _interface[attr] = None

                    available_interfaces[_interface['name']] = namedtuple('Interface', _interface.keys())(**_interface)

                    _interface_found = False
                    _regex_list = None
                    _interface = None
                else:
                    for _regex in _regex_list:
                        _m = re.match(_regex, line)
                        if _m:
                            _details = _m.groupdict()
                            _interface.update(_details)
                            continue

        return available_interfaces


class InterfaceNotFound(Exception):
    """

	"""
    pass
