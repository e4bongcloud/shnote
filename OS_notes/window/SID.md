# 윈도우 보안 식별자, SID(Security Identifier)

윈도우의 각 사용자나 그룹에 부여되는 고유한 식별번호(계정명이 아닌 ID값으로 식별)
사용자가 로그인을 수행하면 접근 토큰이 생성되며, 해당 토큰에는 로그인한 사용자와 그 사용자가 속한 모든 작업 그룹들에 관한 보안 식별자(SID) 정보가 담겨있다.
접근 토큰의 사본은 해당 사용자에 의해 시작된 모든 프로세스에게 할당된다.
윈도우의 계정을 하나의 코드 값으로 표시한 것으로, "whoami /user" 명령어로 로그인 한 사용자의 SID를 확인 할 수 있다.
SID 정보는 SAM 파일(C:\Windows\system32\config\SAM)에 저장된다.

# SID 번호

|        SID       |                  설명                 |
|:----------------:|:-------------------------------------:|
|      S-1-0-0     |       SID를 모를 때 사용하는 SID      |
|      S-1-1-0     |                Everyone               |
|      S-1-5-7     |               Anonymous               |
|     S-1-5-18     | System Profiles(시스템 서비스용 계정) |
|     S-1-5-19     |             Local Service             |
|     S-1-5-20     |            Network Service            |
| S-1-5-domain-500 |             Administrator             |
| S-1-5-domain-501 |                 Guest                 |