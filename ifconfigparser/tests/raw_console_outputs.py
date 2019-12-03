#!/usr/bin/python
# -*- coding: utf-8 -*-

# ======================================================
#
#    File name: test_console_outputs
#    Author: threeheadedknight@protonmail.com
#    Date created: 30.06.2018 17:36
#    Python Version: 3.7
#
# ======================================================
# https://www.computerhope.com/unix/uifconfi.htm
SAMPLE_OUTPUT_LINUX_SYNTAX_1 = """
eth0      Link encap:Ethernet  HWaddr 09:00:12:90:e3:e5
          inet addr:192.168.1.29 Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe70:e3f5/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:54071 errors:1 dropped:0 overruns:0 frame:0
          TX packets:48515 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:22009423 (20.9 MiB)  TX bytes:25690847 (24.5 MiB)
          Interrupt:10 Base address:0xd020

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:83 errors:0 dropped:0 overruns:0 frame:0
          TX packets:83 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:7766 (7.5 KiB)  TX bytes:7766 (7.5 KiB)

wlan0     Link encap:Ethernet  HWaddr 58:a2:c2:93:27:36
          inet addr:192.168.1.64  Bcast:192.168.2.255  Mask:255.255.255.0
          inet6 addr: fe80::6aa3:c4ff:fe93:4746/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:436968 errors:0 dropped:0 overruns:0 frame:0
          TX packets:364103 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:115886055 (110.5 MiB)  TX bytes:83286188 (79.4 MiB)
"""

# http://www.aboutlinux.info/2006/11/ifconfig-dissected-and-demystified.html
SAMPLE_OUTPUT_LINUX_SYNTAX_2 = """
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:480 (480.0 b)  TX bytes:480 (480.0 b)

p2p1      Link encap:Ethernet  HWaddr 00:1C:C0:AE:B5:E6
          inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::21c:c0ff:feae:b5e6/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:41620 errors:0 dropped:0 overruns:0 frame:0
          TX packets:40231 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:21601203 (20.6 MiB)  TX bytes:6145876 (5.8 MiB)
          Interrupt:21 Base address:0xe000
"""

# http://linux-ip.net/html/tools-ifconfig.html
SAMPLE_OUTPUT_LINUX_SYNTAX_3 = """
eth0      Link encap:Ethernet  HWaddr 00:80:C8:F8:4A:51
          inet addr:192.168.99.35  Bcast:192.168.99.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:190312 errors:0 dropped:0 overruns:0 frame:0
          TX packets:86955 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:100
          RX bytes:30701229 (29.2 Mb)  TX bytes:7878951 (7.5 Mb)
          Interrupt:9 Base address:0x5000

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:306 errors:0 dropped:0 overruns:0 frame:0
          TX packets:306 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:29504 (28.8 Kb)  TX bytes:29504 (28.8 Kb)
"""

# http://blmrgnn.blogspot.com/2014/01/linux-ifconfig-command-output-explained.html
SAMPLE_OUTPUT_LINUX_SYNTAX_4 = """
eth0 Link encap:Ethernet  HWaddr 00:0C:29:40:93:9C
     inet addr:192.168.154.102 Bcast:192.168.154.255 Mask:255.255.255.0
     UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
     RX packets:1771 errors:0 dropped:0 overruns:0 frame:0
     TX packets:359 errors:0 dropped:0 overruns:0 carrier:0
     collisions:0 txqueuelen:1000
     RX bytes:138184 (134.9 KiB) TX bytes:49108 (47.9 KiB)
     Interrupt:67 Base address:0x2000

lo   Link encap:Local Loopback
     inet addr:127.0.0.1 Mask:255.0.0.0
     inet6 addr: ::1/128 Scope:Host
     UP LOOPBACK RUNNING MTU:16436 Metric:1
     RX packets:390 errors:0 dropped:0 overruns:0 frame:0
     TX packets:390 errors:0 dropped:0 overruns:0 carrier:0
     collisions:0 txqueuelen:0
     RX bytes:29204 (28.5 KiB) TX bytes:29204 (28.5 KiB)
"""

# https://www.tutorialspoint.com/unix_commands/ifconfig.htm
SAMPLE_OUTPUT_LINUX_SYNTAX_5 = """
eth0      Link encap:Ethernet  HWaddr 00:0c:29:9b:49:bc
          inet addr:192.168.134.128  Bcast:192.168.134.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:fe9b:49bc/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:11545 errors:0 dropped:0 overruns:0 frame:0
          TX packets:6177 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:923360 (923.3 KB)  TX bytes:1712607 (1.7 MB)

eth1      Link encap:Ethernet  HWaddr 00:0c:29:8b:89:bc
          inet addr:  Bcast:  Mask:
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

virbr0    Link encap:Ethernet  HWaddr 3a:bf:4c:fb:90:b6
          inet addr:192.168.122.1  Bcast:192.168.122.255  Mask:255.255.255.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
"""

# http://goinbigdata.com/demystifying-ifconfig-and-network-interfaces-in-linux/
SAMPLE_OUTPUT_LINUX_SYNTAX_6 = """
docker0   Link encap:Ethernet  HWaddr 02:42:2d:66:fc:f1
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:2dff:fe66:fcf1/64 Scope:Link
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:2 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:152 (152.0 B)  TX bytes:258 (258.0 B)

eth0      Link encap:Ethernet  HWaddr 08:00:27:31:65:b5
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::3db9:eaaa:e0ae:6e09/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1089467 errors:0 dropped:0 overruns:0 frame:0
          TX packets:508121 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:903808796 (903.8 MB)  TX bytes:31099448 (31.0 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:9643 errors:0 dropped:0 overruns:0 frame:0
          TX packets:9643 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:719527 (719.5 KB)  TX bytes:719527 (719.5 KB)
"""

# https://ubuntuforums.org/showthread.php?t=2309060
SAMPLE_OUTPUT_LINUX_SYNTAX_7 = """
enp11s0   Link encap:Ethernet  HWaddr 78:2b:cb:ce:1d:92
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
          Interrupt:17

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:902 errors:0 dropped:0 overruns:0 frame:0
          TX packets:902 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:120802 (120.8 KB)  TX bytes:120802 (120.8 KB)

wlp2s0b1  Link encap:Ethernet  HWaddr 68:a3:c4:2f:07:b0
          inet addr:192.168.2.11  Bcast:192.168.2.255  Mask:255.255.255.0
          inet6 addr: fe80::6aa3:c4ff:fe2f:7b0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3542 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2860 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:3080782 (3.0 MB)  TX bytes:377587 (377.5 KB)
"""

# https://ubuntuforums.org/showthread.php?t=2309060
SAMPLE_OUTPUT_LINUX_SYNTAX_8 = """
eth0      Link encap:Ethernet  HWaddr 78:2b:cb:ce:1d:92
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
          Interrupt:17

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:382 errors:0 dropped:0 overruns:0 frame:0
          TX packets:382 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:84203 (84.2 KB)  TX bytes:84203 (84.2 KB)

wlan0     Link encap:Ethernet  HWaddr 68:a3:c4:2f:07:b0
          inet addr:192.168.2.11  Bcast:192.168.2.255  Mask:255.255.255.0
          inet6 addr: fe80::6aa3:c4ff:fe2f:7b0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:242 errors:0 dropped:0 overruns:0 frame:0
          TX packets:256 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:253320 (253.3 KB)  TX bytes:29623 (29.6 KB)
"""

# https://forums.fedoraforum.org/showthread.php?305492-Understanding-ifconfig-command-s-output
SAMPLE_OUTPUT_OPENBSD_SYNTAX_1 = """
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
        inet 0.0.0.0  netmask 255.255.255.0  broadcast 0.0.0.0
        ether 11:11:11:11:11:11  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=820212
SAMPLE_OUTPUT_OPENBSD_SYNTAX_2 = """
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 96.126.108.191  netmask 255.255.255.0  broadcast 96.126.108.255
        inet6 2600:3c03::f03c:91ff:fe70:989d  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::f03c:91ff:fe70:989d  prefixlen 64  scopeid 0x20<link>
        ether f2:3c:91:70:98:9d  txqueuelen 1000  (Ethernet)
        RX packets 8861190  bytes 4193527512 (3.9 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8562901  bytes 3997697400 (3.7 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0:1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.135.145  netmask 255.255.128.0  broadcast 0.0.0.0
        ether f2:3c:91:70:98:9d  txqueuelen 1000  (Ethernet)

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 2988597  bytes 2376311697 (2.2 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2988597  bytes 2376311697 (2.2 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

# https://www.freebsd.org/doc/en_US.ISO8859-1/articles/linux-users/network.html
SAMPLE_OUTPUT_FREEBSD_SYNTAX_1 = """
em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=b<RXCSUM,TXCSUM,VLAN_MTU>
        inet 10.10.10.100 netmask 0xffffff00 broadcast 10.10.10.255
        ether 00:50:56:a7:70:b2
        media: Ethernet autoselect (1000baseTX <full-duplex>)
        status: active
em1: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
        options=b<RXCSUM,TXCSUM,VLAN_MTU>
        inet 192.168.10.222 netmask 0xffffff00 broadcast 192.168.10.255
        ether 00:50:56:a7:03:2b
        media: Ethernet autoselect (1000baseTX <full-duplex>)
        status: active
"""

# https://forums.freebsd.org/threads/loopback-ifconfig-output-different-in-jail.49843/
SAMPLE_OUTPUT_FREEBSD_SYNTAX_2 = """
re0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> metric 0 mtu 1500
  options=8209b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC,LINKSTATE>
  ether b8:97:5a:23:26:32
  media: Ethernet autoselect (none)
  status: no carrier
re1: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
  options=8209b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC,LINKSTATE>
  ether 00:14:d1:2b:9c:b5
  inet 192.168.0.104 netmask 0xffffffff broadcast 192.168.0.104
  media: Ethernet autoselect (1000baseT <full-duplex>)
  status: active
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
  options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
  inet 127.0.0.1 netmask 0xff000000
lo1: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
  options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
  inet 127.0.0.1 netmask 0xffffffff
"""

# https://www.freebsd.org/doc/handbook/config-network-setup.html
SAMPLE_OUTPUT_FREEBSD_SYNTAX_3 = """
dc0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=80008<VLAN_MTU,LINKSTATE>
        ether 00:a0:cc:da:da:da
        inet 192.168.1.3 netmask 0xffffff00 broadcast 192.168.1.255
        media: Ethernet autoselect (100baseTX <full-duplex>)
        status: active
dc1: flags=8802<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=80008<VLAN_MTU,LINKSTATE>
        ether 00:a0:cc:da:da:db
        inet 10.0.0.1 netmask 0xffffff00 broadcast 10.0.0.255
        media: Ethernet 10baseT/UTP
        status: no carrier
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=3<RXCSUM,TXCSUM>
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x4
        inet6 ::1 prefixlen 128
        inet 127.0.0.1 netmask 0xff000000
        nd6 options=3<PERFORMNUD,ACCEPT_RTADV>
"""

# https://github.com/KnightWhoSayNi/ifconfig-parser/files/3898413/ifconfig-osx-10.11.6-2.txt
SAMPLE_OUTPUT_FREEBSD_SYNTAX_4 = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128
	inet 127.0.0.1 netmask 0xff000000
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 68:a8:6d:12:f5:75
	inet6 fe80::6aa8:6dff:fe12:f575%en0 prefixlen 64 scopeid 0x4
	inet6 2600:1700:bab0:d40:6aa8:6dff:fe12:f575 prefixlen 64 autoconf
	inet6 2600:1700:bab0:d40:c0d1:97f7:a613:3ed3 prefixlen 64 autoconf temporary
	inet 192.168.1.81 netmask 0xffffff00 broadcast 192.168.1.255
	inet6 2600:1700:bab0:d40::26 prefixlen 64 dynamic
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: active
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether b2:00:19:cb:f5:50
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 0a:a8:6d:12:f5:75
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 6a:a8:6d:21:38:00
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 5 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
"""

# https://github.com/KnightWhoSayNi/ifconfig-parser/files/3898414/ifconfig-osx-10.11.6.txt
SAMPLE_OUTPUT_FREEBSD_SYNTAX_5 = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128
	inet 127.0.0.1 netmask 0xff000000
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=1<PERFORMNUD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 60:c5:47:0a:ce:0b
	inet6 fe80::62c5:47ff:fe0a:ce0b%en0 prefixlen 64 scopeid 0x4
	inet 192.168.1.65 netmask 0xffffff00 broadcast 192.168.1.255
	inet6 2600:1700:bab0:d40:62c5:47ff:fe0a:ce0b prefixlen 64 autoconf
	inet6 2600:1700:bab0:d40:ad4b:19b2:2ce5:9a1b prefixlen 64 autoconf temporary
	inet6 2600:1700:bab0:d40::2b prefixlen 64 dynamic
	nd6 options=1<PERFORMNUD>
	media: autoselect
	status: active
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether b2:00:14:06:39:21
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 02:c5:47:0a:ce:0b
	media: autoselect
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 62:c5:47:a0:f7:10
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 5 priority 0 path cost 0
	nd6 options=1<PERFORMNUD>
	media: <unknown type>
	status: inactive
"""

# https://github.com/KnightWhoSayNi/ifconfig-parser/files/3898415/ifconfig-osx-10.14.6-2.txt
SAMPLE_OUTPUT_FREEBSD_SYNTAX_6 = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
XHC0: flags=0<> mtu 0
XHC1: flags=0<> mtu 0
XHC20: flags=0<> mtu 0
VHC128: flags=0<> mtu 0
en5: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether ac:de:48:00:10:20
	inet6 fe80::aede:48ff:fe00:1020%en5 prefixlen 64 scopeid 0x8
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (100baseTX <full-duplex>)
	status: active
ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
	ether a6:83:e7:2d:63:8e
	media: autoselect
	status: inactive
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether a4:83:e7:2d:63:8e
	inet6 fe80::4dd:cbd7:2743:da63%en0 prefixlen 64 secured scopeid 0xa
	inet 192.168.1.221 netmask 0xffffff00 broadcast 192.168.1.255
	inet6 2600:1700:bab0:d40:1874:4566:6499:f3d1 prefixlen 64 autoconf secured
	inet6 2600:1700:bab0:d40:30d4:c067:a56d:5888 prefixlen 64 deprecated autoconf temporary
	inet6 2600:1700:bab0:d40:342e:1ac7:8bdb:6c3d prefixlen 64 deprecated autoconf temporary
	inet6 2600:1700:bab0:d40:fdd1:e943:edd4:5187 prefixlen 64 autoconf temporary
	inet6 2600:1700:bab0:d40::39 prefixlen 64 dynamic
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 06:83:e7:2d:63:8e
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether 7e:05:c1:24:14:ca
	inet6 fe80::7c05:c1ff:fe24:14ca%awdl0 prefixlen 64 scopeid 0xc
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether ea:00:fd:08:58:02
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether ea:00:fd:08:58:01
	media: autoselect <full-duplex>
	status: inactive
en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether ea:00:fd:08:58:06
	media: autoselect <full-duplex>
	status: inactive
en4: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether ea:00:fd:08:58:05
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether ea:00:fd:08:58:02
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 13 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 14 priority 0 path cost 0
	member: en3 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 15 priority 0 path cost 0
	member: en4 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 16 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::7b12:adc2:a089:c4d8%utun0 prefixlen 64 scopeid 0x12
	nd6 options=201<PERFORMNUD,DAD>
vmnet1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 00:50:56:c0:00:01
	inet 192.168.101.1 netmask 0xffffff00 broadcast 192.168.101.255
vmnet8: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 00:50:56:c0:00:08
	inet 192.168.71.1 netmask 0xffffff00 broadcast 192.168.71.255
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::a08a:46aa:a738:2ea7%utun1 prefixlen 64 scopeid 0x15
	nd6 options=201<PERFORMNUD,DAD>
"""

# https://github.com/KnightWhoSayNi/ifconfig-parser/files/3898416/ifconfig-osx-10.14.6.txt
SAMPLE_OUTPUT_FREEBSD_SYNTAX_7 = """
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
XHC1: flags=0<> mtu 0
XHC0: flags=0<> mtu 0
XHC20: flags=0<> mtu 0
en5: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether ac:de:48:00:13:23
	inet6 fe80::aede:48ff:fe00:1323%en5 prefixlen 64 scopeid 0x7
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether f0:18:98:03:d9:30
	inet6 fe80::8b7:1281:7499:b504%en0 prefixlen 64 secured scopeid 0x8
	inet 192.168.1.72 netmask 0xffffff00 broadcast 192.168.1.255
	inet6 2600:1700:bab0:d40:bb:9ad:34c5:2e9a prefixlen 64 autoconf secured
	inet6 2600:1700:bab0:d40:4573:9380:5ecb:ef52 prefixlen 64 autoconf temporary
	inet6 2600:1700:bab0:d40::24 prefixlen 64 dynamic
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 02:18:98:03:f8:49
	media: autoselect
	status: inactive
awdl0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1484
	ether 1e:06:52:da:9b:86
	inet6 fe80::1c06:52ff:feda:9b86%awdl0 prefixlen 64 scopeid 0xa
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 02:00:31:81:83:05
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 02:00:31:81:94:10
	media: autoselect <full-duplex>
	status: inactive
en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 02:00:31:81:94:06
	media: autoselect <full-duplex>
	status: inactive
en4: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=60<TSO4,TSO6>
	ether 02:00:31:81:94:05
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 02:00:31:81:94:02
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x2
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 11 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 12 priority 0 path cost 0
	member: en3 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 13 priority 0 path cost 0
	member: en4 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 14 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::cec:23d0:8cf7:c88e%utun0 prefixlen 64 scopeid 0x10
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::cf42:647e:9077:7bcb%utun1 prefixlen 64 scopeid 0x11
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::f67f:be47:695a:f5b1%utun2 prefixlen 64 scopeid 0x12
	nd6 options=201<PERFORMNUD,DAD>
utun3: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::2998:653d:a6da:9ca5%utun3 prefixlen 64 scopeid 0x13
	nd6 options=201<PERFORMNUD,DAD>
utun4: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::8e0f:4631:2328:5209%utun4 prefixlen 64 scopeid 0x14
	nd6 options=201<PERFORMNUD,DAD>
"""
