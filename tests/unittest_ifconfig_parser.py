#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: unittest_ifconfig_parser
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:03
#    Python Version: 3.6
#
# ======================================================
import logging
import unittest

from ifconfig_parser import IfconfigParser
from tests.test_console_outputs import *


class TestIfconfigParser(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_001(self):
		console_output = LINUX_SYNTAX_SAMPLE_4
		interfaces = IfconfigParser(console_output=console_output)

		all_interfaces = interfaces.list_interfaces()
		print(all_interfaces)

		a = interfaces.get_interface('eth0')
		print(a)

		b = interfaces.filter_interfaces(mtu='1500', mac_addr='00:e3:f7:2c:a0:46')
		print(b)

		b = interfaces.filter_interfaces(mtu='1500')
		print(b)

		b = interfaces.filter_interfaces(mac_addr='00:e3:f7:2c:a0:46')
		print(b)

		b = interfaces.filter_interfaces(ipv4_addr='10.20.174.232')
		print(b)

		c = interfaces.filter_interfaces(mtu='1500', ipv4_addr='10.20.174.233')
		print(c)


if __name__ == '__main__':
	unittest.main()
