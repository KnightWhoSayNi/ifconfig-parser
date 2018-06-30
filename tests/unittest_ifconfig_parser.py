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
from tests.test_console_outputs import UBUNTU_IFCONFIG_16


class TestIfconfigParser(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_001(self):
		console_output = UBUNTU_IFCONFIG_16
		interfaces = IfconfigParser(console_output=console_output)


if __name__ == '__main__':
	unittest.main()
