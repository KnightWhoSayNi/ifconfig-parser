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


class IfconfigParser(object):

	def __init__(self, console_output):

		if isinstance(console_output, list):
			source_data = console_output
		else:
			source_data = console_output.splitlines()
		self.interfaces = self.parser(source_data=source_data)

	def __del__(self):
		pass

	def list_interfaces(self):
		pass

	def filter_interfaces(self, query):
		pass

	def get_interface(self, name):
		pass

	def get_interfaces(self):
		return self.interfaces

	@staticmethod
	def parser(source_data):

		# Linux syntax

		re_linux_interface = re.compile(
			r"(?P<interface_name>[a-zA-Z0-9:._-]+)\s+Link encap\:(?P<interface_type>\S+)\s+HWaddr\s+\b(?P<interface_mac_addr>[0-9A-Fa-f:?]+)",
			re.I)
		re_linux_ipv4 = re.compile(
			r"inet addr:(?P<interface_ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+Bcast:(?P<interface_ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+Mask:(?P<interface_ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})",
			re.I)
		re_linux_ipv6 = re.compile(
			r"inet6 addr:\s+(?P<interface_ipv6_addr>\S+)\/(?P<interface_ipv6_mask>[0-9]+)\s+Scope:(?P<interface_ipv6_scope>Link)",
			re.I)
		re_linux_state = re.compile(
			r"(?P<interface_state>.*)\s+MTU:(?P<interface_mtu>[0-9]+)\s+Metric:(?P<interface_metric>[0-9]+)", re.I)
		re_linux_rx = re.compile(
			r"RX packets:(?P<interface_rx_packets>[0-9]+)\s+errors:(?P<interface_rx_errors>[0-9]+)\s+dropped:(?P<interface_rx_dropped>[0-9]+)\s+overruns:(?P<interface_rx_overruns>[0-9]+)\s+frame:(?P<interface_rx_frame>[0-9]+)",
			re.I)
		re_linux_tx = re.compile(
			r"TX packets:(?P<interface_tx_packets>[0-9]+)\s+errors:(?P<interface_tx_errors>[0-9]+)\s+dropped:(?P<interface_tx_dropped>[0-9]+)\s+overruns:(?P<interface_tx_overruns>[0-9]+)\s+carrier:(?P<interface_tx_carrier>[0-9]+)",
			re.I)
		re_linux_tx_stats = re.compile(r"collisions:(?P<interface_tx_collisions>[0-9]+)\s+txqueuelen:[0-9]+", re.I)
		re_linux = [re_linux_ipv4, re_linux_ipv6, re_linux_state, re_linux_rx, re_linux_tx, re_linux_tx_stats]
		# OpenBSD syntax

		re_openbsd_interface = re.compile(
			r"(?P<interface_name>[a-zA-Z0-9:._-]+):\s+flags=(?P<interface_flags>[0-9]+)<(?P<interface_state>\S+)>\s+mtu\s+(?P<interface_mtu>[0-9]+)",
			re.I)
		re_openbsd_ipv4 = re.compile(
			r"inet (?P<interface_ipv4_addr>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+netmask\s+(?P<interface_ipv4_mask>(?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+broadcast\s+(?P<interface_ipv4_bcast>(?:[0-9]{1,3}\.){3}[0-9]{1,3})",
			re.I)
		re_openbsd_ipv6 = re.compile(
			r"inet6\s+(?P<interface_ipv6_addr>\S+)\s+prefixlen\s+(?P<interface_ipv6_mask>[0-9]+)\s+scopeid\s+[0-9]+x[0-9]+<(?P<interface_ipv6_scope>link)>",
			re.I)
		re_openbsd_details = re.compile(
			r"\S+\s+(?P<interface_mac_addr>[0-9A-Fa-f:?]+)\s+txqueuelen\s+[0-9]+\s+\((?P<interface_type>\S+)\)", re.I)
		re_openbsd_rx = re.compile(r"RX packets (?P<interface_rx_packets>[0-9]+)\s+bytes.*", re.I)
		re_openbsd_rx_stats = re.compile(
			r"RX errors (?P<interface_rx_errors>[0-9]+)\s+dropped\s+(?P<interface_rx_dropped>[0-9]+)\s+overruns\s+(?P<interface_rx_overruns>[0-9]+)\s+frame\s+(?P<interface_rx_frame>[0-9]+)",
			re.I)
		re_openbsd_tx = re.compile(r"TX packets (?P<interface_tx_packets>[0-9]+)\s+bytes.*", re.I)
		re_openbsd_tx_stats = re.compile(
			r"TX errors (?P<interface_tx_errors>[0-9]+)\s+dropped\s+(?P<interface_tx_dropped>[0-9]+)\s+overruns\s+(?P<interface_tx_overruns>[0-9]+)\s+carrier\s+(?P<interface_tx_carrier>[0-9]+)\s+collisions\s+(?P<interface_tx_collisions>[0-9]+)",
			re.I)
		re_openbsd = [re_openbsd_interface, re_openbsd_ipv4, re_openbsd_ipv6, re_openbsd_details, re_openbsd_rx, re_openbsd_rx_stats, re_openbsd_tx, re_openbsd_tx_stats]

		# FreeBSD syntax
		# TODO: Add regular expressions

		inter = dict()

		_interface_found = False
		_interface_details = None
		_regex_list = None

		lines = len(source_data)
		for index, line in enumerate(source_data):
			line = line.strip()
			if not _interface_found:
				m_linux = re.match(re_linux_interface, line)
				if m_linux:
					_interface_found = True
					_regex_list = re_linux
					_interface_details = m_linux.groupdict()
					continue
				m_openbsd = re.match(re_openbsd_interface, line)
				if m_openbsd:
					_interface_found = True
					_regex_list = re_openbsd
					_interface_details = m_openbsd.groupdict()
					continue
			else:
				if line == '' or index == (lines - 1):
					_interface_found = False
					inter[_interface_details['interface_name']] = _interface_details
					_interface_details = None
				else:
					if _regex_list is not None:
						for _regex in _regex_list:
							_m = re.match(_regex, line)
							if _m:
								_details = _m.groupdict()
								_interface_details = {**_interface_details, **_details}
								continue

		return inter
