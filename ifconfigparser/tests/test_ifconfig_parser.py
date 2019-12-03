#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: unittest_ifconfig_parser
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:03
#    Python Version: 3.7
#
# ======================================================
import unittest

from collections import namedtuple
from ifconfig_parser import IfconfigParser, InterfaceNotFound
from raw_console_outputs import *


class TestIfconfigParser(unittest.TestCase):

    def setUp(self):
        self.details = []

    def tearDown(self):
        del self.details

    def verify(self, parser):

        for i in parser.get_interfaces():
            self.assertTrue(parser.is_available(name=i))
            self.assertIn(i, parser.list_interfaces())

        with self.assertRaises(InterfaceNotFound):
            parser.get_interface(name='NONSENSE')

        self.assertFalse(parser.is_available(name='NONSENSE'))

        for name, attr_test in self.details:
            interface_target = parser.get_interface(name=name)
            interface_ref = self.generate_interface(attr=attr_test)
            self.compare_attributes(attr_target=interface_target, attr_ref=interface_ref)

    def generate_interface(self, attr):

        all_attr = ['name', 'type', 'mac_addr', 'ipv4_addr', 'ipv4_bcast', 'ipv4_mask', 'ipv6_addr', 'ipv6_mask',
        'ipv6_scope', 'state', 'mtu', 'metric', 'rx_packets', 'rx_errors', 'rx_dropped', 'rx_overruns',
        'rx_frame', 'tx_packets', 'tx_errors', 'tx_dropped', 'tx_overruns', 'tx_carrier', 'tx_collisions',
        'rx_bytes', 'tx_bytes']

        for a in all_attr:
            if not attr.get(a):
                attr[a] = None

        interface = namedtuple("Interface", attr)(**attr)

        return interface

    def compare_attributes(self, attr_target, attr_ref):

        self.assertEqual(attr_target.state, attr_ref.state)
        self.assertEqual(attr_target.type, attr_ref.type)
        self.assertEqual(attr_target.mac_addr, attr_ref.mac_addr)
        self.assertEqual(attr_target.ipv4_addr, attr_ref.ipv4_addr)
        self.assertEqual(attr_target.ipv4_bcast, attr_ref.ipv4_bcast)
        self.assertEqual(attr_target.ipv4_mask, attr_ref.ipv4_mask)
        self.assertEqual(attr_target.ipv6_addr, attr_ref.ipv6_addr)
        self.assertEqual(attr_target.ipv6_mask, attr_ref.ipv6_mask)
        self.assertEqual(attr_target.ipv6_scope, attr_ref.ipv6_scope)
        self.assertEqual(attr_target.mtu, attr_ref.mtu)
        self.assertEqual(attr_target.rx_packets, attr_ref.rx_packets)
        self.assertEqual(attr_target.rx_errors, attr_ref.rx_errors)
        self.assertEqual(attr_target.rx_dropped, attr_ref.rx_dropped)
        self.assertEqual(attr_target.rx_overruns, attr_ref.rx_overruns)
        self.assertEqual(attr_target.rx_frame, attr_ref.rx_frame)
        self.assertEqual(attr_target.tx_packets, attr_ref.tx_packets)
        self.assertEqual(attr_target.tx_errors, attr_ref.tx_errors)
        self.assertEqual(attr_target.tx_dropped, attr_ref.tx_dropped)
        self.assertEqual(attr_target.tx_overruns, attr_ref.tx_overruns)
        self.assertEqual(attr_target.tx_carrier, attr_ref.tx_carrier)
        self.assertEqual(attr_target.tx_collisions, attr_ref.tx_collisions)
        self.assertEqual(attr_target.metric, attr_ref.metric)
        self.assertEqual(attr_target.rx_bytes, attr_ref.rx_bytes)
        self.assertEqual(attr_target.tx_bytes, attr_ref.tx_bytes)

    def test_generic(self):

        console_output = ""
        interfaces = IfconfigParser(console_output=console_output)

        self.assertIsInstance(interfaces, IfconfigParser)

        self.assertIsInstance(interfaces.count_interfaces(), int)
        self.assertEqual(interfaces.count_interfaces(), 0)

        self.assertIsInstance(interfaces.list_interfaces(), list)
        self.assertEqual(interfaces.list_interfaces(), [])

        self.assertIsInstance(interfaces.filter_interfaces(name="NONSENSE"), list)
        self.assertEqual(interfaces.filter_interfaces(name="NONSENSE"), [])

        with self.assertRaises(InterfaceNotFound):
            interfaces.get_interface(name='NONSENSE')

        self.assertFalse(interfaces.is_available(name='NONSENSE'))

        # Template
        # _name = ""
        # _ref = {'name': _name, 'type': '', 'mac_addr': '', 'ipv4_addr': '', 'ipv4_bcast': '', 'ipv4_mask': '', 'ipv6_addr': '', 'ipv6_mask': '',
        #         'ipv6_scope': '', 'state': '', 'mtu': '', 'metric': '', 'rx_packets': '', 'rx_errors': '', 'rx_dropped': '', 'rx_overruns': '',
        #         'rx_frame': '', 'tx_packets': '', 'tx_errors': '', 'tx_dropped': '', 'tx_overruns': '', 'tx_carrier': '', 'tx_collisions': ''}
        # self.details.append((_name, _ref))
        #
        # self.verify(parser=interfaces)

    def test_linux_syntax_001(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_1
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '09:00:12:90:e3:e5',
        'ipv4_addr': '192.168.1.29', 'ipv4_bcast': '192.168.1.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::a00:27ff:fe70:e3f5', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1',
        'rx_packets': '54071', 'rx_errors': '1', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '48515', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '22009423', 'tx_bytes': '25690847'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '16436', 'metric': '1', 'rx_packets': '83', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '83', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '7766', 'tx_bytes': '7766'}
        self.details.append((_name, _ref))

        _name = "wlan0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '58:a2:c2:93:27:36', 'ipv4_addr': '192.168.1.64',
        'ipv4_bcast': '192.168.2.255', 'ipv4_mask': '255.255.255.0', 'ipv6_addr': 'fe80::6aa3:c4ff:fe93:4746', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '436968',
        'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0', 'rx_frame': '0', 'tx_packets': '364103', 'tx_errors': '0',
        'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '115886055', 'tx_bytes': '83286188'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_002(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_2
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '16436', 'metric': '1', 'rx_packets': '8', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '8', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '480', 'tx_bytes': '480'}
        self.details.append((_name, _ref))

        _name = "p2p1"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:1C:C0:AE:B5:E6', 'ipv4_addr': '192.168.0.1', 'ipv4_bcast': '192.168.0.255', 'ipv4_mask': '255.255.255.0', 'ipv6_addr': 'fe80::21c:c0ff:feae:b5e6', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '41620', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '40231', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '21601203', 'tx_bytes': '6145876'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_003(self):

        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_3
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:80:C8:F8:4A:51', 'ipv4_addr': '192.168.99.35', 'ipv4_bcast': '192.168.99.255', 'ipv4_mask': '255.255.255.0',
        'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '190312', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '86955', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '30701229', 'tx_bytes': '7878951'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0',
        'state': 'UP LOOPBACK RUNNING', 'mtu': '16436', 'metric': '1', 'rx_packets': '306', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '306', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '29504', 'tx_bytes': '29504'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_004(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_4
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:0C:29:40:93:9C', 'ipv4_addr': '192.168.154.102',
        'ipv4_bcast': '192.168.154.255', 'ipv4_mask': '255.255.255.0',
        'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '1771', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '359', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '138184', 'tx_bytes': '49108'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '16436', 'metric': '1', 'rx_packets': '390', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '390', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '29204', 'tx_bytes': '29204'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_005(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_5
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 4)

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:0c:29:9b:49:bc', 'ipv4_addr': '192.168.134.128', 'ipv4_bcast': '192.168.134.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::20c:29ff:fe9b:49bc', 'ipv6_mask': '64', 'ipv6_scope': 'Link',
        'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '11545', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '6177', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '923360', 'tx_bytes': '1712607'}
        self.details.append((_name, _ref))

        _name = "eth1"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:0c:29:8b:89:bc', 'ipv6_addr': 'fe80::20c:29ff:fe9b:49bc', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '11545', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '6177', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '923360', 'tx_bytes': '1712607'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '65536', 'metric': '1', 'rx_packets': '0', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        _name = "virbr0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '3a:bf:4c:fb:90:b6', 'ipv4_addr': '192.168.122.1', 'ipv4_bcast': '192.168.122.255', 'ipv4_mask': '255.255.255.0',
        'state': 'UP BROADCAST MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '0', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_006(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_6
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "docker0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '02:42:2d:66:fc:f1', 'ipv4_addr': '172.17.0.1', 'ipv4_bcast': '0.0.0.0', 'ipv4_mask': '255.255.0.0', 'ipv6_addr': 'fe80::42:2dff:fe66:fcf1', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '2', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '3', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '152', 'tx_bytes': '258'}
        self.details.append((_name, _ref))

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '08:00:27:31:65:b5', 'ipv4_addr': '10.0.2.15', 'ipv4_bcast': '10.0.2.255', 'ipv4_mask': '255.255.255.0', 'ipv6_addr': 'fe80::3db9:eaaa:e0ae:6e09', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '1089467', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '508121', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '903808796', 'tx_bytes': '31099448'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '65536', 'metric': '1', 'rx_packets': '9643', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '9643', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '719527', 'tx_bytes': '719527'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_007(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_7
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "enp11s0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '78:2b:cb:ce:1d:92',
        'state': 'UP BROADCAST MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '0', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '65536', 'metric': '1', 'rx_packets': '902', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '902', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '120802', 'tx_bytes': '120802'}
        self.details.append((_name, _ref))

        _name = "wlp2s0b1"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '68:a3:c4:2f:07:b0', 'ipv4_addr': '192.168.2.11', 'ipv4_bcast': '192.168.2.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::6aa3:c4ff:fe2f:7b0', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '3542', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '2860', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '3080782', 'tx_bytes': '377587'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_linux_syntax_008(self):
        console_output = SAMPLE_OUTPUT_LINUX_SYNTAX_8
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "eth0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '78:2b:cb:ce:1d:92',
        'state': 'UP BROADCAST MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '0', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': 'Host', 'state': 'UP LOOPBACK RUNNING', 'mtu': '65536', 'metric': '1', 'rx_packets': '382', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '382', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '84203', 'tx_bytes': '84203'}
        self.details.append((_name, _ref))

        _name = "wlan0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '68:a3:c4:2f:07:b0', 'ipv4_addr': '192.168.2.11', 'ipv4_bcast': '192.168.2.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::6aa3:c4ff:fe2f:7b0', 'ipv6_mask': '64',
        'ipv6_scope': 'Link', 'state': 'UP BROADCAST RUNNING MULTICAST', 'mtu': '1500', 'metric': '1', 'rx_packets': '242', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '256', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '253320', 'tx_bytes': '29623'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_openbsd_syntax_001(self):
        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_1
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "enp2s0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,MULTICAST',
        'mtu': '1500', 'mac_addr': 'aa:aa:aa:aa:aa:aa', 'ipv4_addr': '0.0.0.100',
        'ipv4_mask': '255.255.255.0', 'ipv4_bcast': '0.0.0.0',
        'ipv6_addr': 'aaaa::aaaa:aaaa:aaaa:aaaa', 'ipv6_mask': '64', 'ipv6_scope': '0x20',
        'type': 'Ethernet', 'rx_packets': '64219', 'rx_errors': '0', 'rx_dropped': '0',
        'rx_overruns': '0', 'rx_frame': '0', 'tx_packets': '37986', 'tx_errors': '0',
        'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '82340039', 'tx_bytes': '4117999'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING', 'mtu': '65536',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1',
        'ipv6_mask': '128', 'ipv6_scope': '0x10', 'type': 'Local Loopback',
        'rx_packets': '12', 'rx_errors': '0', 'rx_dropped': '0',
        'rx_overruns': '0', 'rx_frame': '0', 'tx_packets': '12', 'tx_errors': '0',
        'tx_dropped': '0', 'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0',
        'rx_bytes': '1596', 'tx_bytes': '1596'}
        self.details.append((_name, _ref))

        _name = "virbr0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,MULTICAST', 'mtu': '1500',
        'ipv4_addr': '0.0.0.0', 'ipv4_mask': '255.255.255.0', 'ipv4_bcast': '0.0.0.0',
        'mac_addr': '11:11:11:11:11:11', 'type': 'Ethernet', 'rx_packets': '0',
        'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0', 'rx_frame': '0',
        'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0', 'tx_overruns': '0',
        'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_openbsd_syntax_002(self):
        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_2
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = 'eth0'
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': 'f2:3c:91:70:98:9d',
        'ipv4_addr': '96.126.108.191', 'ipv4_bcast': '96.126.108.255',
        'ipv4_mask': '255.255.255.0', 'ipv6_addr': 'fe80::f03c:91ff:fe70:989d', 'ipv6_mask': '64',
        'ipv6_scope': '0x20', 'state': 'UP,BROADCAST,RUNNING,MULTICAST', 'mtu': '1500',
        'rx_packets': '8861190', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '8562901', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '4193527512', 'tx_bytes': '3997697400'}
        self.details.append((_name, _ref))

        _name = 'eth0:1'
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': 'f2:3c:91:70:98:9d',
        'ipv4_addr': '192.168.135.145', 'ipv4_bcast': '0.0.0.0',
        'ipv4_mask': '255.255.128.0', 'state': 'UP,BROADCAST,RUNNING,MULTICAST', 'mtu': '1500'}
        self.details.append((_name, _ref))

        _name = 'lo'
        _ref = {'name': _name, 'type': 'Local Loopback',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0', 'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': '0x10', 'state': 'UP,LOOPBACK,RUNNING', 'mtu': '65536',
        'rx_packets': '2988597', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '2988597', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '2376311697', 'tx_bytes': '2376311697'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_openbsd_syntax_003(self):

        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_3
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "docker0"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '02:42:1a:0a:77:e4',
        'ipv4_addr': '172.17.0.1', 'ipv4_bcast': '0.0.0.0', 'ipv4_mask': '255.255.0.0',
        'state': 'UP,BROADCAST,MULTICAST', 'mtu': '1500',
        'rx_packets': '0', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '0', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '0', 'tx_bytes': '0'}
        self.details.append((_name, _ref))

        _name = "ens33"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:0c:29:3b:58:0e',
        'ipv4_addr': '192.168.71.138', 'ipv4_bcast': '192.168.71.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::c1cb:715d:bc3e:b8a0', 'ipv6_mask': '64',
        'ipv6_scope': '0x20', 'state': 'UP,BROADCAST,RUNNING,MULTICAST', 'mtu': '1500',
        'rx_packets': '62408', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '25974', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '23770378', 'tx_bytes': '3523483'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0',
        'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': '0x10', 'state': 'UP,LOOPBACK,RUNNING', 'mtu': '65536',
        'rx_packets': '37068', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '37068', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '14181021', 'tx_bytes': '14181021'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)


    def test_openbsd_syntax_004(self):

        console_output = SAMPLE_OUTPUT_OPENBSD_SYNTAX_4
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        _name = "ens33"
        _ref = {'name': _name, 'type': 'Ethernet', 'mac_addr': '00:0c:29:99:45:17',
        'ipv4_addr': '192.168.71.131', 'ipv4_bcast': '192.168.71.255', 'ipv4_mask': '255.255.255.0',
        'ipv6_addr': 'fe80::20c:29ff:fe99:4517', 'ipv6_mask': '64',
        'ipv6_scope': '0x20', 'state': 'UP,BROADCAST,RUNNING,MULTICAST', 'mtu': '1500',
        'rx_packets': '35444', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '9940', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '38714337', 'tx_bytes': '995718'}
        self.details.append((_name, _ref))

        _name = "lo"
        _ref = {'name': _name, 'type': 'Local Loopback',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '255.0.0.0',
        'ipv6_addr': '::1', 'ipv6_mask': '128',
        'ipv6_scope': '0x10', 'state': 'UP,LOOPBACK,RUNNING', 'mtu': '65536',
        'rx_packets': '331', 'rx_errors': '0', 'rx_dropped': '0', 'rx_overruns': '0',
        'rx_frame': '0', 'tx_packets': '331', 'tx_errors': '0', 'tx_dropped': '0',
        'tx_overruns': '0', 'tx_carrier': '0', 'tx_collisions': '0', 'rx_bytes': '29530', 'tx_bytes': '29530'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_001(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_1
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 2)

        _name = "em0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '00:50:56:a7:70:b2', 'ipv4_addr': '10.10.10.100',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '10.10.10.255'}
        self.details.append((_name, _ref))

        _name = "em1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '00:50:56:a7:03:2b', 'ipv4_addr': '192.168.10.222',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.10.255'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_002(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_2
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 4)

        _name = "re0"
        _ref = {'name': _name, 'state': 'BROADCAST,SIMPLEX,MULTICAST', 'mtu': '1500',
        'mac_addr': 'b8:97:5a:23:26:32', 'metric': '0'}
        self.details.append((_name, _ref))

        _name = "re1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '00:14:d1:2b:9c:b5', 'ipv4_addr': '192.168.0.104',
        'ipv4_mask': '0xffffffff', 'ipv4_bcast': '192.168.0.104', 'metric': '0'}
        self.details.append((_name, _ref))

        _name = "lo0"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST', 'mtu': '16384',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000', 'metric': '0'}
        self.details.append((_name, _ref))

        _name = "lo1"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST', 'mtu': '16384',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xffffffff', 'metric': '0'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_003(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_3
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 3)

        _name = "dc0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST', 'mtu': '1500', 'ipv4_addr': '192.168.1.3',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.1.255', 'mac_addr': '00:a0:cc:da:da:da', 'metric': '0'}
        self.details.append((_name, _ref))

        _name = 'dc1'
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST', 'mtu': '1500',
        'ipv4_addr': '10.0.0.1', 'ipv4_mask': '0xffffff00', 'ipv4_bcast': '10.0.0.255',
        'mac_addr': '00:a0:cc:da:da:db', 'metric': '0'}
        self.details.append((_name, _ref))

        _name = 'lo0'
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST', 'mtu': '16384',
        'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000', 'ipv6_addr': 'fe80::1',
        'ipv6_mask': '64', 'ipv6_scope': '0x4', 'metric': '0'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_004(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_4
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 7)

        _name = "lo0"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST',
        'mtu': '16384', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000',
        'ipv6_addr': 'fe80::1', 'ipv6_mask': '64', 'ipv6_scope': '0x1'}
        self.details.append((_name, _ref))

        _name = "gif0"
        _ref = {'name': _name, 'state': 'POINTOPOINT,MULTICAST', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "stf0"
        _ref = {'name': _name, 'state': '', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "en0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '68:a8:6d:12:f5:75', 'ipv4_addr': '192.168.1.81',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.1.255',
        'ipv6_addr': 'fe80::6aa8:6dff:fe12:f575', 'ipv6_mask': '64', 'ipv6_scope': '0x4'}
        self.details.append((_name, _ref))

        _name = "en1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX',
        'mtu': '1500', 'mac_addr': 'b2:00:19:cb:f5:50'}
        self.details.append((_name, _ref))

        _name = "p2p0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '2304', 'mac_addr': '0a:a8:6d:12:f5:75'}
        self.details.append((_name, _ref))

        _name = "bridge0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '6a:a8:6d:21:38:00'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_005(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_5
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 7)

        _name = "lo0"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST',
        'mtu': '16384', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000',
        'ipv6_addr': 'fe80::1', 'ipv6_mask': '64', 'ipv6_scope': '0x1'}
        self.details.append((_name, _ref))

        _name = "gif0"
        _ref = {'name': _name, 'state': 'POINTOPOINT,MULTICAST', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "stf0"
        _ref = {'name': _name, 'state': '', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "en0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '60:c5:47:0a:ce:0b', 'ipv4_addr': '192.168.1.65',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.1.255', 'ipv6_addr': 'fe80::62c5:47ff:fe0a:ce0b',
        'ipv6_mask': '64', 'ipv6_scope': '0x4'}
        self.details.append((_name, _ref))

        _name = "en1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX',
        'mtu': '1500', 'mac_addr': 'b2:00:14:06:39:21'}
        self.details.append((_name, _ref))

        _name = "p2p0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '2304', 'mac_addr': '02:c5:47:0a:ce:0b'}
        self.details.append((_name, _ref))

        _name = "bridge0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '62:c5:47:a0:f7:10'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_006(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_6
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 21)

        _name = "lo0"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST',
        'mtu': '16384', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000',
        'ipv6_addr': 'fe80::1', 'ipv6_mask': '64', 'ipv6_scope': '0x1'}
        self.details.append((_name, _ref))

        _name = "gif0"
        _ref = {'name': _name, 'state': 'POINTOPOINT,MULTICAST', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "stf0"
        _ref = {'name': _name, 'state': '', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "XHC0"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "XHC1"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "XHC20"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "VHC128"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "en5"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ac:de:48:00:10:20', 'ipv6_addr': 'fe80::aede:48ff:fe00:1020',
        'ipv6_mask': '64', 'ipv6_scope': '0x8'}
        self.details.append((_name, _ref))

        _name = "ap1"
        _ref = {'name': _name, 'state': 'BROADCAST,SIMPLEX,MULTICAST', 'mtu': '1500',
        'mac_addr': 'a6:83:e7:2d:63:8e'}
        self.details.append((_name, _ref))

        _name = "en0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'a4:83:e7:2d:63:8e', 'ipv4_addr': '192.168.1.221',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.1.255',
        'ipv6_addr': 'fe80::4dd:cbd7:2743:da63', 'ipv6_mask': '64', 'ipv6_scope': '0xa'}
        self.details.append((_name, _ref))

        _name = "p2p0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '2304', 'mac_addr': '06:83:e7:2d:63:8e'}
        self.details.append((_name, _ref))

        _name = "awdl0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1484', 'mac_addr': '7e:05:c1:24:14:ca', 'ipv6_addr': 'fe80::7c05:c1ff:fe24:14ca',
        'ipv6_mask': '64', 'ipv6_scope': '0xc'}
        self.details.append((_name, _ref))

        _name = "en1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ea:00:fd:08:58:02'}
        self.details.append((_name, _ref))

        _name = "en2"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ea:00:fd:08:58:01'}
        self.details.append((_name, _ref))

        _name = "en3"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ea:00:fd:08:58:06'}
        self.details.append((_name, _ref))

        _name = "en4"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ea:00:fd:08:58:05'}
        self.details.append((_name, _ref))

        _name = "bridge0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ea:00:fd:08:58:02'}
        self.details.append((_name, _ref))

        _name = "utun0"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '2000', 'ipv6_addr': 'fe80::7b12:adc2:a089:c4d8', 'ipv6_mask': '64',
        'ipv6_scope': '0x12'}
        self.details.append((_name, _ref))

        _name = "vmnet1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '00:50:56:c0:00:01', 'ipv4_addr': '192.168.101.1',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.101.255'}
        self.details.append((_name, _ref))

        _name = "vmnet8"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '00:50:56:c0:00:08', 'ipv4_addr': '192.168.71.1',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.71.255'}
        self.details.append((_name, _ref))

        _name = "utun1"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '1380', 'ipv6_addr': 'fe80::a08a:46aa:a738:2ea7', 'ipv6_mask': '64',
        'ipv6_scope': '0x15'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)

    def test_freebsd_syntax_007(self):
        console_output = SAMPLE_OUTPUT_FREEBSD_SYNTAX_7
        interfaces = IfconfigParser(console_output=console_output)

        self.assertEqual(interfaces.count_interfaces(), 20)

        _name = "lo0"
        _ref = {'name': _name, 'state': 'UP,LOOPBACK,RUNNING,MULTICAST',
        'mtu': '16384', 'ipv4_addr': '127.0.0.1', 'ipv4_mask': '0xff000000',
        'ipv6_addr': 'fe80::1', 'ipv6_mask': '64', 'ipv6_scope': '0x1'}
        self.details.append((_name, _ref))

        _name = "gif0"
        _ref = {'name': _name, 'state': 'POINTOPOINT,MULTICAST', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "stf0"
        _ref = {'name': _name, 'state': '', 'mtu': '1280'}
        self.details.append((_name, _ref))

        _name = "XHC1"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "XHC0"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "XHC20"
        _ref = {'name': _name, 'state': '', 'mtu': '0'}
        self.details.append((_name, _ref))

        _name = "en5"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'ac:de:48:00:13:23', 'ipv6_addr': 'fe80::aede:48ff:fe00:1323',
        'ipv6_mask': '64', 'ipv6_scope': '0x7'}
        self.details.append((_name, _ref))

        _name = "en0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': 'f0:18:98:03:d9:30', 'ipv4_addr': '192.168.1.72',
        'ipv4_mask': '0xffffff00', 'ipv4_bcast': '192.168.1.255',
        'ipv6_addr': 'fe80::8b7:1281:7499:b504', 'ipv6_mask': '64', 'ipv6_scope': '0x8'}
        self.details.append((_name, _ref))

        _name = "p2p0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '2304', 'mac_addr': '02:18:98:03:f8:49'}
        self.details.append((_name, _ref))

        _name = "awdl0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1484', 'mac_addr': '1e:06:52:da:9b:86', 'ipv6_addr': 'fe80::1c06:52ff:feda:9b86',
        'ipv6_mask': '64', 'ipv6_scope': '0xa'}
        self.details.append((_name, _ref))

        _name = "en1"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '02:00:31:81:83:05'}
        self.details.append((_name, _ref))

        _name = "en2"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '02:00:31:81:94:10'}
        self.details.append((_name, _ref))

        _name = "en3"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '02:00:31:81:94:06'}
        self.details.append((_name, _ref))

        _name = "en4"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '02:00:31:81:94:05'}
        self.details.append((_name, _ref))

        _name = "bridge0"
        _ref = {'name': _name, 'state': 'UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST',
        'mtu': '1500', 'mac_addr': '02:00:31:81:94:02'}
        self.details.append((_name, _ref))

        _name = "utun0"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '2000', 'ipv6_addr': 'fe80::cec:23d0:8cf7:c88e', 'ipv6_mask': '64',
        'ipv6_scope': '0x10'}
        self.details.append((_name, _ref))

        _name = "utun1"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '1380', 'ipv6_addr': 'fe80::cf42:647e:9077:7bcb', 'ipv6_mask': '64',
        'ipv6_scope': '0x11'}
        self.details.append((_name, _ref))

        _name = "utun2"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '1380', 'ipv6_addr': 'fe80::f67f:be47:695a:f5b1', 'ipv6_mask': '64',
        'ipv6_scope': '0x12'}
        self.details.append((_name, _ref))

        _name = "utun3"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '1380', 'ipv6_addr': 'fe80::2998:653d:a6da:9ca5', 'ipv6_mask': '64',
        'ipv6_scope': '0x13'}
        self.details.append((_name, _ref))

        _name = "utun4"
        _ref = {'name': _name, 'state': 'UP,POINTOPOINT,RUNNING,MULTICAST',
        'mtu': '1380', 'ipv6_addr': 'fe80::8e0f:4631:2328:5209', 'ipv6_mask': '64',
        'ipv6_scope': '0x14'}
        self.details.append((_name, _ref))

        self.verify(parser=interfaces)


if __name__ == '__main__':
    unittest.main()
