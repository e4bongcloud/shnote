# 룰 추가 or 삭제 

``` bash
iptables --insert <chain> <rulenum> <options> <target>
```

* `--insert `: 새로운 rule을 체인 중간에 추가함

``` bash
iptables --append INPUT <options> <target>
```

* `--append` : 새로운 rule을 체인 맨 끝에 추가함

