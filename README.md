# ifconfig-parser

[![Build Status](https://travis-ci.org/KnightWhoSayNi/ifconfig-parser.svg?branch=master)](https://travis-ci.org/KnightWhoSayNi/ifconfig-parser) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/KnightWhoSayNi/ifconfig-parser/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ifconfig-parser) ![PyPI](https://img.shields.io/pypi/v/ifconfig-parser) [![Downloads](https://pepy.tech/badge/ifconfig-parser)](https://pepy.tech/project/ifconfig-parser) [![Downloads](https://pepy.tech/badge/ifconfig-parser/month)](https://pepy.tech/project/ifconfig-parser/month) [![Downloads](https://pepy.tech/badge/ifconfig-parser/week)](https://pepy.tech/project/ifconfig-parser/week) 

Unsophisticated python package for parsing raw output of [ifconfig](https://en.wikipedia.org/wiki/Ifconfig). 

## Getting Started

Install **ifconfig-parser** from [pypi](https://pypi.org/project/ifconfig-parser/)

```shell
pip install ifconfig-parser
```

Supported attributes of network interfaces:
- name
- type
- mac_addr
- ipv4_addr
- ipv4_bcast
- ipv4_mask
- ipv6_addr
- ipv6_mask
- ipv6_scope
- state
- mtu
- metric
- rx_packets
- rx_errors
- rx_dropped
- rx_overruns
- rx_frame
- tx_packets
- tx_errors
- tx_dropped
- tx_overruns
- tx_carrier
- tx_collisions

## Usage


#### Import

Initialization

```python
>>> from ifconfigparser import IfconfigParser
>>> 
>>> console_output = """
enp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 0.0.0.100  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 aaaa::aaaa:aaaa:aaaa:aaaa  prefixlen 64  scopeid 0x20<link>
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 64219  bytes 82340039 (78.5 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 37986  bytes 4117999 (3.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 12  bytes 1596 (1.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12  bytes 1596 (1.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 0.0.0.0  netmask 255.255.255.0  broadcast 0.0.0.0.0
        ether 11:11:11:11:11:11  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""
>>> interfaces = IfconfigParser(console_output=console_output)
```

#### list_interfaces()

List names of all available network interfaces
```python
>>> interfaces.list_interfaces()
['enp2s0', 'lo', 'virbr0']
```

#### count_interfaces()

Number of all available network interfaces
```python
>>> interfaces.count_interfaces()
3
```

#### get_interfaces()

List details of all available network interfaces
```python
>>> interfaces.get_interfaces()
{'enp2s0': Interface(name='enp2s0', flags='4163', state='UP,BROADCAST,RUNNING,MULTICAST', mtu='1500', ipv4_addr='0.0.0.100', ipv4_mask='255.255.255.0', ipv4_bcast='0.0.0.0', ipv6_addr='aaaa::aaaa:aaaa:aaaa:aaaa', ipv6_mask='64', ipv6_scope='link', mac_addr='aa:aa:aa:aa:aa:aa', type='Ethernet', rx_packets='64219', rx_errors='0', rx_dropped='0', rx_overruns='0', rx_frame='0', tx_packets='37986', tx_errors='0', tx_dropped='0', tx_overruns='0', tx_carrier='0', tx_collisions='0', metric=None), 'lo': Interface(name='lo', flags='73', state='UP,LOOPBACK,RUNNING', mtu='65536', ipv4_addr='127.0.0.1', ipv4_mask='255.0.0.0', ipv4_bcast=None, ipv6_addr='::1', ipv6_mask='128', ipv6_scope='host', mac_addr=None, type='Local Loopback', rx_packets='12', rx_errors='0', rx_dropped='0', rx_overruns='0', rx_frame='0', tx_packets='12', tx_errors='0', tx_dropped='0', tx_overruns='0', tx_carrier='0', tx_collisions='0', metric=None), 'virbr0': Interface(name='virbr0', flags='4099', state='UP,BROADCAST,MULTICAST', mtu='1500', ipv4_addr='0.0.0.0', ipv4_mask='255.255.255.0', ipv4_bcast='0.0.0.0', mac_addr='11:11:11:11:11:11', type='Ethernet', rx_packets='0', rx_errors='0', rx_dropped='0', rx_overruns='0', rx_frame='0', tx_packets='0', tx_errors='0', tx_dropped='0', tx_overruns='0', tx_carrier='0', tx_collisions='0', ipv6_addr=None, ipv6_mask=None, ipv6_scope=None, metric=None)}
```

#### get_interface()

List details of a particular network interface
```python
>>> interfaces.get_interface(name="lo")
Interface(name='lo', flags='73', state='UP,LOOPBACK,RUNNING', mtu='65536', ipv4_addr='127.0.0.1', ipv4_mask='255.0.0.0', ipv4_bcast=None, ipv6_addr='::1', ipv6_mask='128', ipv6_scope='host', mac_addr=None, type='Local Loopback', rx_packets='12', rx_errors='0', rx_dropped='0', rx_overruns='0', rx_frame='0', tx_packets='12', tx_errors='0', tx_dropped='0', tx_overruns='0', tx_carrier='0', tx_collisions='0', metric=None)
```

#### filter_interfaces()

Filter network interfaces by attribute(s)
```python
>>> interfaces.filter_interfaces(mtu='1500')
['enp2s0', 'virbr0']
>>> interfaces.filter_interfaces(mtu='1500', name='enp2s0')
['enp2s0']
```

#### is_available()

Is a network interface available
```python
>>> interfaces.is_available(name='enp2s0')
True
```


#### Exceptions 

Raise **InterfaceNotFound** in case of missing interface
```python
>>> interfaces.get_interface(name="eth0")
    raise InterfaceNotFound("Interface [{}] not found.".format(name))
ifconfigparser.ifconfig_parser.InterfaceNotFound: Interface [eth0] not found.
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
