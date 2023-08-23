# 점검 방법
Cisco IOS

``` bash
Router# show running-config
```

# Session time 설정

## Console
``` bash
Router# config terminal
Router(config)# line con 0
Router(config-line)# exec-timeout 5 0
```

## VTY
``` bash
Router# config terminal
Router(config)# line vty 0 4
Router(config-line)# exec-timeout 5 0
```
## AUX

``` bash
Router# config terminal
Router(config)# line aux 0
Router(config-line)# exec-timeout 5 0
```