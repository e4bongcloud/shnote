# DNS 조회순서
``` cmd
C:\Windows\System32\drivers\etc\hosts 
```
# dns 조회 순서
1. 로컬 DNS 캐시(Local DNS Cache)
2. 호스트 파일(Hosts File)
3. DNS 클라이언트 설정(DNS Client Configuration)
4. DNS 서버 순회(DNS Server Lookup

# local DNS cache

``` cmd
C:\Users\dbstj>ipconfig /displaydns

Windows IP Configuration

    1.0.25.172.in-addr.arpa
    ----------------------------------------
    Record Name . . . . . : 1.0.25.172.in-addr.arpa.
    Record Type . . . . . : 12
    Time To Live  . . . . : 167077
    Data Length . . . . . : 8
    Section . . . . . . . : Answer
    PTR Record  . . . . . : DESKTOP-3R4QLRE.mshome.net


    desktop-3r4qlre.mshome.net
    ----------------------------------------
    No records of type AAAA


    desktop-3r4qlre.mshome.net
    ----------------------------------------
    Record Name . . . . . : DESKTOP-3R4QLRE.mshome.net
    Record Type . . . . . : 1
    Time To Live  . . . . : 167077
    Data Length . . . . . : 4
    Section . . . . . . . : Answer
    A (Host) Record . . . : 172.25.0.1
```

``` cmd
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
# Added by Docker Desktop
192.168.55.116 host.docker.internal
192.168.55.116 gateway.docker.internal
# To allow the same kube context to work on the host and the container:
127.0.0.1 kubernetes.docker.internal
# End of section
```

