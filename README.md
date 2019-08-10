# ifconfig-parser

[![Build Status](https://travis-ci.org/KnightWhoSayNi/ifconfig-parser.svg?branch=master)](https://travis-ci.org/KnightWhoSayNi/ifconfig-parser) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/KnightWhoSayNi/ifconfig-parser/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ifconfig-parser) ![PyPI](https://img.shields.io/pypi/v/ifconfig-parser) [![Downloads](https://pepy.tech/badge/ifconfig-parser)](https://pepy.tech/project/ifconfig-parser) [![Downloads](https://pepy.tech/badge/ifconfig-parser/month)](https://pepy.tech/project/ifconfig-parser/month) [![Downloads](https://pepy.tech/badge/ifconfig-parser/week)](https://pepy.tech/project/ifconfig-parser/week) 

Unsophisticated python package for parsing raw output of [ifconfig](https://en.wikipedia.org/wiki/Ifconfig). It supports Linux, OpenBSD and FreeBSD syntax.  

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
... em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
...         options=b<RXCSUM,TXCSUM,VLAN_MTU>
...         inet 10.10.10.100 netmask 0xffffff00 broadcast 10.10.10.255
...         ether 00:50:56:a7:70:b2
...         media: Ethernet autoselect (1000baseTX <full-duplex>)
...         status: active
... em1: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
...         options=b<RXCSUM,TXCSUM,VLAN_MTU>
...         inet 192.168.10.222 netmask 0xffffff00 broadcast 192.168.10.255
...         ether 00:50:56:a7:03:2b
...         media: Ethernet autoselect (1000baseTX <full-duplex>)
...         status: active
... """
>>> interfaces = IfconfigParser(console_output=console_output)
```

#### list_interfaces()

List names of all available network interfaces
```python
>>> interfaces.list_interfaces()
['em0', 'em1']
```

#### count_interfaces()

List number of all available network interfaces
```python
>>> interfaces.count_interfaces()
2
```

#### get_interfaces()

List details of all available network interfaces
```python
>>> interfaces.get_interfaces()
{'em0': Interface(name='em0', flags='8843', state='UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST', mtu='1500', type=None, mac_addr=None, ipv4_addr=None, ipv4_bcast=None, ipv4_mask=None, ipv6_addr=None, ipv6_mask=None, ipv6_scope=None, metric=None, rx_packets=None, rx_errors=None, rx_dropped=None, rx_overruns=None, rx_frame=None, tx_packets=None, tx_errors=None, tx_dropped=None, tx_overruns=None, tx_carrier=None, tx_collisions=None), 'em1': Interface(name='em1', flags='8843', state='UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST', mtu='1500', type=None, mac_addr=None, ipv4_addr=None, ipv4_bcast=None, ipv4_mask=None, ipv6_addr=None, ipv6_mask=None, ipv6_scope=None, metric=None, rx_packets=None, rx_errors=None, rx_dropped=None, rx_overruns=None, rx_frame=None, tx_packets=None, tx_errors=None, tx_dropped=None, tx_overruns=None, tx_carrier=None, tx_collisions=None)}
```

#### get_interface()

List details of a particular network interface
```python
>>> interfaces.get_interface(name="em0")
Interface(name='em0', flags='8843', state='UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST', mtu='1500', type=None, mac_addr=None, ipv4_addr=None, ipv4_bcast=None, ipv4_mask=None, ipv6_addr=None, ipv6_mask=None, ipv6_scope=None, metric=None, rx_packets=None, rx_errors=None, rx_dropped=None, rx_overruns=None, rx_frame=None, tx_packets=None, tx_errors=None, tx_dropped=None, tx_overruns=None, tx_carrier=None, tx_collisions=None)
```

#### filter_interfaces()

Filter network interfaces by attribute(s)
```python
>>> interfaces.filter_interfaces(mtu='1500')
['em0', 'em1']
>>> interfaces.filter_interfaces(mtu='1500', name='em1')
['em1']
```

#### Exceptions 

Raise **InterfaceNotFound** in case of missing interface
```python
>>> interfaces.get_interface(name="lo")
    raise InterfaceNotFound("Interface [{}] not found.".format(name))
ifconfigparser.ifconfig_parser.InterfaceNotFound: Interface [lo] not found.
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
