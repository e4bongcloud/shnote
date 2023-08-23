# 쿠키 보안 취약점

## XSS(Cross-Site Scripting) 공격

웹 사이트를 만들기 위해서 HTML언어로 페이지를 구성해야하는데 HTML만으로 정적인 페이지를 만들수가 없다.

그래서 서버 사이드 스크립트 언어인 PHP, JSP, ASP 등 CGI(Common Gateway Interface) 프로그램을 이용해야된다

XSS 공격은 자바스크립트가 사용자의 컴퓨터에서 실행된다는 점을 이용한 공격입니다. 자바스크립트에서 "document.cookie"라는 명령어는 사이트에서 쿠키 값을 활용할 수 있게 하는 역할을 하지만 공격자들은 쿠키 값을 탈취하기 위해서 사용하기도 합니다.
    
### XSS 대응법




## 스니핑(Sniffing) 공격

스니핑이란 단어의 사전적 의미는 '코를 훌쩍이는, 킁킁거리며 냄새를 맡는' 입니다. 사전적 의미와 같이 스니핑 공격은 네트워크의 중간에서 남의 패킷 정보를 도청하는 해킹 유형의 하나입니다. 수동적 공격에 해당하며, 도청할 수 있도록 설치되는 도구를 스니퍼(Sniffer)라고 합니다.

우리가 웹 페이지에 쿠키를 사용할 경우 서버와 클라이언트는 매번 요청 때마다 쿠키를 주고받게 됩니다. 이때 네트워크 상에 전달되는 쿠키가 스니핑 공격에 의해서 탈취당할 수 있습니다.


## 공용 PC에서 쿠키값 유출

쿠키는 사용자의 하드디스크에 저장되기 때문에 공용 PC인 경우 쿠키를 쉽게 탈취할 수 있습니다. 사용자 개인이 주의해서 사용해야 할 문제인 것 같습니다.


## HTML5 웹 스토리지 정보 유출