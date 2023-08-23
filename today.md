USB-type-C Thunderbolt 정리

Firebolt

CATV

TOKEN-BUS

XSMA

TOKEN-RING

ATM shell
데이터를 셸에다가 패킷을 넘기는 패킷망
(상용화 못함)

802.14 WB(Why Bro)

SNTP
라우터를 위한 프로토콜

DNS SNMP

비접속형(Connectionless) 
	전달되는 데이터그램에 대해 상태 정보 유지하지 않음
	Best-Effort 서비스

IPv6 Flow Lable
	비슷한 기능을 하는 ip구조를 가진것들의 연산을 더 빠르게 처리하기위해 만듬
test

http 프로토콜을 사용하여 세션을 유지하는 
세션
쿠키
hidden type
url rewriting

# 저장 
https://groups.google.com/g/security-onion/c/KC5GlhM5RVw/discussion


# 신호변환장치(DCE)
DCE(Data Circuit-terminal Equipment)

 Data Circuit-terminal Equipment
 네트워크를 연결하는 물리적인 수단을 관리 및 처리
 데이터에 대한 변조 후 전송회선(전송로)용 신호 생성
 전송로를 통해 수신된 신호에 대한 복조를 수행(예: 모뎀(MODEM))

# DTE
 Data Terminal Equipment
 사용자와 인터페이스를 이루는 종단 장치(End Device / Terminal)
 일반적으로 디지털 신호를 처리하는 시스템(예: 컴퓨터, 라우터, 스마트폰 등)
 원격의 종단장치와 통신을 위해서는 별도의 DCE(Data Circuit-terminal Equipment) 장치가 필요
* 라우터도 DTE다.

 통신제어장치(CCU)
 Communication Control Unit
 데이터 전송 제어 기능을 수행
 데이터 전송계와 처리계의 사이(단순한 1:1통신일 경우 생략이 가능)
 접속, 통신 방식, 경로 설정, 다중 접속 제어를 수행

통신회선 개수에 따른 분류
 물리 매체(전송회선)가 전송 장치(모뎀 등)에 연결된 통신회선의 개수에 따라 분류
 2선식 또는 4선식
• 2선식(2W, 2Wires)
– 신호선과 공통 접지선의 2개로 구성
– 양방향 통신에서 위/아래로 전송할 때 동일한 전송로를 사용
• 4선식(4W, 4Wires)
– 신호선과 공통 접지선의 4개로 구성
– 양방향 통신에서 위/아래로 전송할 때 별도의 전송로를 사용

접속 방식에 따른 종류
 점-대-점 회선 방식 (Point-to-Point Line)
 다지점 회선 방식(Multipoint Line)
 집선 회선 방식(Line Concentration)
 회선 다중 방식(Line Multiplexing)

점-대-점 회선 방식 (Point-to-Point Line)
 컴퓨터 시스템과 단말기를 전용회선으로 직접 연결
 주로 고속 처리에 이용
 구 전화회선
 장점: 빠른 응답
 단점: 회선 구축에 많은 비용이 듦
 예: 컴퓨터와 주변기기(예: 키보드, 마우스)의 관계


 다지점 회선 방식(Multipoint / Multidrop Line)
 컴퓨터 시스템에 연결된 전송회선 1개에 단말기를 여러 대 연결
 예: USB허브를 통한 주변 장치 연결
 폴링(Polling)
• 단말기에서 컴퓨터로 데이터를 전송할 때 사용
• 컴퓨터 감시 프로그램에서 신호를 보내 송신할 데이터가 있는지 주기적으로 검사
 선택(Selection)
• 컴퓨터에서 특정 단말기를 지정하여 데이터를 전송할 때 주로 이용
• 일반적으로 특정 단말기를 지정하는 제어 문자를 데이터 앞에 포함시켜 전송
• 경제적, 짧은 시간 동안 회선을 운영하므로 주로 조회 처리할 때 사용
 경쟁(Contention)
• 단말 장치가 서로 경쟁하면서 회선에 접근하는 방법
• 가장 간단하지만 효율적이지 않음


# RSS(Really Simple Syndication, Rich Site Summary)
 블로그처럼 컨텐츠 업데이트가 자주 일어나는 웹사이트에서, 업데이트된 정보를 쉽게 구독자들에게 제공하기 위해 XML을 기초로 만들어진 데이터 형식입니다.

# 라이브러리
실제 코드와 api 둘다 제공하는 서비스
# api
상호작용 부분만을 위한 서비스

프레임워크 = 재사용 가능한 코드를 제공하지만  IOC(제어권이 프레임워크에 있다.) 

DI(Dependency Injection)
프레임워크가 객체를 호출하고, 의존성이 필요한 경우 프레임워크가 연결


AOP(Aspect Oriented Programming)
핵심적인 비즈니스 로직과 관련이 없고, 여러 곳에서 공통적으로 사용되는 기능을 분리하여 실행 시 조합하는 방식

CID란?

IPO(Input Process Output)

curl --include --request GET 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRouteSt?serviceKey=5dcOQw9ejNSFsPHn1NIKNOQmwYFPRqSjtKbJkkEiAJQ7fwDy1MZJ1%2Fc6rRd8zYMNDEUJqPvjC8wHae8AHLNZ8w%3D%3D&busRouteId=152&startOrd=1&endOrd=10'


JPA

Beans란

컨테이너


하이퍼바이저란?

PRS(완전순방향 비밀성, Perfect Forward )

Secrecy

RFC 5246

Poodle

RC4

pingbed 

session splicing

DHCP DORA

FCS

https://www.bluesplatter.com/is_certification/ISCert-04IS-02AccessControl/

# 2023-03-22

CRC 연산

CCITT

ITUT

X.509

DSU

– 폴링 : 단말기에서 컴퓨터로 데이터를 전송하는 데 사용
– 선택 : 컴퓨터가 특정 단말기를 지정하여 데이터를 전송하는 데 사용, 데이터 앞에 특정 단말기를 지정하
는 제어 문자를 포함

오류를 검출하는 방식
– 패리티 검사(Parity Bit Check)
– 블록 합 검사(BSC: Block Sum Check)
– 순환 중복(CRC: Cycle Redundancy Check) 

버퍼란 무엇인가

스텍이란 무엇인가

동기화란 무엇인가

프론트홀과 백홀

DC RU DU 란? 네트워크에서 

RAN 이란

ngfw

바이콜라

맨처스터 방식 

IEEE 802.3 프로토콜

XON: 데이터 중단 해제 및 재개
XOFF: 데이터 통신 중단


# Sliding Window
* 기존 ARQ 방식을 기반(Go-Back N, Selective Repeat ARQ)
* 송신 측은 지정된 윈도 크기만큼 프레임들을 연속해서 전송하는 방식
* 송신데이터의 오류 및 소실 등을 모니터링하여 윈도의 크기를 가변