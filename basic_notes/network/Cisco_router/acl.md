# VTY 접근 허용 IP 설정
``` bash
Router# config terminal
Router(config)# access-list <ACL 번호> permit <IP 주소> 
Router(config)# access-list <ACL 번호> deny any log 
Router(config)# line vty ?
<0X4> First Line number
Router(config)# line vty 0 4
Router(config)# access-class <ACL 번호> in
```

