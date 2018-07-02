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
        inet 0.0.0.0  netmask 255.255.255.0  broadcast 0.0.0.0.0
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