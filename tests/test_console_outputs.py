#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: test_console_outputs
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:36
#    Python Version: 3.6
#
# ======================================================
LINUX_SYNTAX_SAMPLE_1 = """
docker0   Link encap:Ethernet  HWaddr BF:55:55:B2:72:72
          inet addr:79.39.199.76  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::5ceb:dff:fe67:c00b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:174726 errors:0 dropped:0 overruns:0 frame:0
          TX packets:203060 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:44283923 (42.2 MiB)  TX bytes:138178316 (131.7 MiB)

eth0      Link encap:Ethernet  HWaddr 18:73:73:DC:2C:2C
          inet addr:106.120.103.238  Bcast:106.120.103.255  Mask:255.255.255.0
          inet6 addr: fe80::1a03:73ff:fedc:1c2c/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8288644 errors:0 dropped:0 overruns:0 frame:0
          TX packets:949272 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:884192592 (843.2 MiB)  TX bytes:953073340 (908.9 MiB)
          Interrupt:20 Memory:e1a00000-e1a20000

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:9405 errors:0 dropped:0 overruns:0 frame:0
          TX packets:9405 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:481883 (470.5 KiB)  TX bytes:481883 (470.5 KiB)

veth1b0ab78 Link encap:Ethernet  HWaddr BF:30:30:B2:33:33
          inet6 addr: fe80::b072:33ff:febf:3055/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:27506 errors:0 dropped:0 overruns:0 frame:0
          TX packets:22367 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:4096869 (3.9 MiB)  TX bytes:2651040 (2.5 MiB)
"""

LINUX_SYNTAX_SAMPLE_2 = """
docker0   Link encap:Ethernet  HWaddr BF:55:55:B2:B2:33
          inet addr:79.39.199.76  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::5ceb:dff:fe67:c00b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:174726 errors:0 dropped:0 overruns:0 frame:0
          TX packets:203060 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:44283923 (42.2 MiB)  TX bytes:138178316 (131.7 MiB)

eth0      Link encap:Ethernet  HWaddr 18:73:73:DC:2C:2C
          inet addr:106.120.103.238  Bcast:106.120.103.255  Mask:255.255.255.0
          inet6 addr: fe80::1a03:73ff:fedc:1c2c/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:8288644 errors:0 dropped:0 overruns:0 frame:0
          TX packets:949272 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:884192592 (843.2 MiB)  TX bytes:953073340 (908.9 MiB)
          Interrupt:20 Memory:e1a00000-e1a20000

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:9405 errors:0 dropped:0 overruns:0 frame:0
          TX packets:9405 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:481883 (470.5 KiB)  TX bytes:481883 (470.5 KiB)

veth1b0ab78 Link encap:Ethernet  HWaddr BF:30:B2:B2:72:33
          inet6 addr: fe80::b072:33ff:febf:3055/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:27506 errors:0 dropped:0 overruns:0 frame:0
          TX packets:22367 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:4096869 (3.9 MiB)  TX bytes:2651040 (2.5 MiB)
"""

LINUX_SYNTAX_SAMPLE_3 = """
eth0      Link encap:Ethernet  HWaddr DE:10:32:D5:E1:E1
          inet addr:106.120.103.190  Bcast:106.120.103.255  Mask:255.255.255.0
          inet6 addr: fe80::dc10:32ff:fed5:5fe1/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:35787350 errors:0 dropped:0 overruns:0 frame:0
          TX packets:7299647 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:14219423765 (13.2 GiB)  TX bytes:14697982576 (13.6 GiB)
          Interrupt:36

eth1      Link encap:Ethernet  HWaddr 4A:5D:08:4A:8E:8A
          inet addr:10.20.174.187  Bcast:10.20.174.255  Mask:255.255.255.0
          inet6 addr: 2001:10:20:174:485d:8ff:feb6:8e8a/64 Scope:Global
          inet6 addr: fe80::485d:8ff:feb6:8e8a/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:11130879 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1348116 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1046531408 (998.0 MiB)  TX bytes:7916730115 (7.3 GiB)
          Interrupt:35

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:120848677 errors:0 dropped:0 overruns:0 frame:0
          TX packets:120848677 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:18671244487 (17.3 GiB)  TX bytes:18671244487 (17.3 GiB)
"""

LINUX_SYNTAX_SAMPLE_4 = """
eth0      Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.20  Bcast:10.20.174.255  Mask:255.255.255.0
          inet6 addr: 2001:10:20:174:20a:f7ff:fe2c:e346/64 Scope:Global
          inet6 addr: fe80::20a:f7ff:fe2c:e346/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:27112295 errors:0 dropped:0 overruns:0 frame:0
          TX packets:105042790 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:28316352097 (28.3 GB)  TX bytes:156243474122 (156.2 GB)
          Interrupt:16

eth0:0    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.210  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:1    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.211  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:2    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.212  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:3    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.213  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:4    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.214  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:5    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.215  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:6    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.216  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:7    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.217  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:8    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.218  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:9    Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.219  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:10   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.220  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:11   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.221  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:12   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.222  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:13   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.223  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:14   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.224  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:15   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.225  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:16   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.226  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:17   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.227  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:18   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.228  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:19   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.229  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:20   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.230  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:22   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.232  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:23   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.233  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:24   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.234  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:25   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.235  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:26   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.236  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:27   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.237  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:28   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.238  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:29   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.239  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth0:30   Link encap:Ethernet  HWaddr 00:e3:f7:2c:a0:46
          inet addr:10.20.174.240  Bcast:10.20.174.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          Interrupt:16

eth1      Link encap:Ethernet  HWaddr 18:03:73:bd:b7:7a
          inet addr:106.120.103.14  Bcast:106.120.103.255  Mask:255.255.255.0
          inet6 addr: fe80::6c9:e39a:f5f0:f78c/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:28158306 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1912808 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:2150843002 (2.1 GB)  TX bytes:1196728984 (1.1 GB)
          Interrupt:20 Memory:e1b00000-e1b20000

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:55541 errors:0 dropped:0 overruns:0 frame:0
          TX packets:55541 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:5319949 (5.3 MB)  TX bytes:5319949 (5.3 MB)
"""

OPENBSD_SYNTAX_SAMPLE_1 = """
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.38  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::fac1:992c:c511:f808  prefixlen 64  scopeid 0x20<link>
        inet6 2a02:a31b:443:c900:494:c644:9beb:ffc5  prefixlen 64  scopeid 0x0<global>
        ether b8:89:eb:a1:a1:89  txqueuelen 1000  (Ethernet)
        RX packets 67622  bytes 92301911 (88.0 MiB)
        RX errors 0  dropped 1  overruns 0  frame 0
        TX packets 36821  bytes 3274218 (3.1 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 9  bytes 524 (524.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 9  bytes 524 (524.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

OPENBSD_SYNTAX_SAMPLE_2 = """
eth0      Link encap:Ethernet  HWaddr 00:0c:49:9b:0c:bc
          inet addr:192.168.134.128  Bcast:192.168.134.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe9b:49bc/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:11545 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6177 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:923360 (923.3 KB)  TX bytes:1712607 (1.7 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

virbr0    Link encap:Ethernet  HWaddr 3a:fb:4c:fb:bf:b6
          inet addr:192.168.122.1  Bcast:192.168.122.255  Mask:255.255.255.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
"""
