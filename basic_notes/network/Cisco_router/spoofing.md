# spoofing deny
스푸핑 방지 예시
``` bash
router# configure terminal
router(config)# access-list <ACL 번호> deny ip 0.0.0.0 0.255.255.255 any
router(config)# access-list <ACL 번호> deny ip 10.0.0.0 0.255.255.255 any
router(config)# access-list <ACL 번호> deny ip 127.0.0.0 0.255.255.255 any
router(config)# access-list <ACL 번호> deny ip 169.254.0.0 0.0.255.255 any
router(config)# access-list <ACL 번호> deny ip 172.16.0.0 0.15.255.255 any
router(config)# access-list <ACL 번호> deny ip 192.0.2.0 0.0.0.255 any
router(config)# access-list <ACL 번호> deny ip 192.168.0.0 0.0.255.255 any
router(config)# access-list <ACL 번호> deny ip 224.0.0.0 15.255.255.255 any
router(config)# access-list <ACL 번호> permit ip any any
``시