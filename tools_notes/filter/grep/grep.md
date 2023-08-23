```bash 
ls | grep 'text`
```

# 파일안 내용을 찾는 명령어 조합

```bash
grep -rnw 'pwd' -e 'pattern'
```

# test 파일을 제외하고 찾기
``` bash
grep -v "test"
```

# test와 dodo 파일을 제외하고 찾기  
( -E 옵션은 확장정규식으로 기존 정규식을 개선시킨 정규식이다.)
``` bash
grep -vE "test|dodo"
```
