# sysctl
커널 변수의 값을 제어하여 시스템을 최적화할 수 있는 명령이다. sysctl은 시스템의 `/proc/sys` 디렉터리 밑에 있는 커널 매개변수를 제어한다.  

# sysctl 명령어

``` bash
sysctl [options] [variable[=value] ...]
```

``` bash
-n: 특정 변수의 값을 출력합니다.
-w: 특정 변수의 값을 설정합니다.
-p: /etc/sysctl.conf 파일에 저장된 설정을 읽어서 변수 값을 설정합니다.
```


``` bash
sysctl -a
```

``` bash
sysctl -n kernel.hostname
```

``` bash
sysctl -w net.ipv4.tcp_rmem='4096 87380 10485760'
sysctl -w net.ipv4.tcp_wmem='4096 87380 10485760'
```

``` bash
sysctl -p
```