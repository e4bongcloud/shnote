# SNMP service check

``` bash
Router# show running-config
Router# show snmp
```

# SNMP 켜기 

# SNMP 끄기
``` bash
Router# config terminal
Router(config)# no snmp-server
```

# SNMP ACL 설정
``` bash
Router# config terminal
Router(config)# access-list <ACL 번호> permit <IP 주소>
Router(config)# access-list <ACL 번호> deny any log 
Router(config)# snmp-server community <커뮤니티 스트링> RO <ACL 번호>
```

# SNP 커뮤니티 권한

``` bash
Router# config terminal
Router(config)# snmp-server community <스트링명> RO
Router(config)# snmp-server community <스트링명> RW
```

