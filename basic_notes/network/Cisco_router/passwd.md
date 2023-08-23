# enable 패스워드 설정

``` bash
Router# config terminal 
Router(config)# enable secret [Passwd]
```
or

``` bash
Router(config)# enable password [Passwd]
Router(config)# end
Router#
```

# 가상 터미널 패스워드 설정 
``` bash
Router# config terminal
Router(config)# line vty ?
<0X4> First Line number
Router(config)# line vty 0 4
Router(config-line)# login
Router(config-line)# password [Passwd]
```

# 콘솔 패스워드 설정
``` bash
Router# config terminal
Router(config)# line console ?
<0X0> First Line number
Router(config)# line console 0
Router(config-line)# login
Router(config-line)# password [Passwd]
```

# 보조(AUX) 포트 패스워드 설정

``` bash
Router# config terminal
Router(config)# line aux ?
<0X0> First Line number
Router(config)# line aux 0
Router(config-line)# login
Router(config-line)# password  [Passwd]
```
