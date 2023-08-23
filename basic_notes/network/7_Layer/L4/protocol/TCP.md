# tcp 플래그 

![tcp_header](https://www.gatevidyalay.com/wp-content/uploads/2018/09/TCP-Header-Format.png)

| 구조              | 크기  | 설명                     |
| ----------------- | ----- | ----------------------- |
| Source Port       | 16bit | 운영체제내 송신 프로세스의 주소 <br> 응용프로그램을 식별하기 위해 운영체제에 의해 동적인 번호로 할당된다.|
| Destination Port  | 16bit | 수신 프로세스의 주소 <br> 수신 포트는 서버 구동 시 할당된다.|
| Sequence Number   | 32bit | TCP 세그먼트의 일련번호 <br> 일련번호느느 세그먼트 별 1씩 증가 <br> 세그먼트의 누락을 해결, 순서 교정 및 중복 세그먼트를 방지한다.|
| Acknowledge Number| 32bit | 다음 번에 수신될 것으로 예상되는 세그먼트의 번호 |
| Header Length     | 4bit  | 헤더의 크기(지정 크기 x4, 기본값: 101b) <br> - 기본값: 0101b = 5 -> 20bytes(5*4) <br> 이 값을 통해, 세그먼트내 데이터(SDU)의 시작 위치를 알 수 있다. |
| Reserve           | 6bit  | 미래를 위해 남겨놓은 영역 <br> 현재까지 사용되지 않는다. |
| Flag Bits         | 6bit  | 회선, 데이터의 관리와 제어 기능 등을 수행하는 영역 |
| Window Size       | 16bit | 데이터를 전송할 때 수신측에서 한 번에 받을 수 있는 최대 데이터 양을 나타내는 값입니다. 수신측은 이 값을 보고 한 번에 받을 데이터의 양을 결정합니다.|
| Checksum          | 16bit | TCP 세그먼트 전체의 오류를 검출하기 위해 사용되는 값으로, 송신측이 데이터를 보낼 때 계산하여 첨부합니다. 수신측은 체크섬 값을 다시 계산하여 오류가 발생했는지 확인합니다. |
| Urgent Pointer    | 16bit | 긴급 데이터의 위치를 가리키는 값으로, 수신측은 이 값을 보고 긴급 데이터를 우선적으로 처리합니다.|
| Options           | 32bit | TCP 헤더에 포함될 수 있는 여러 가지 정보를 담고 있습니다. 예를 들어 MSS(Maximum Segment Size) 옵션은 한 번에 전송 가능한 최대 TCP 세그먼트 크기를 지정하는 옵션입니다.| 

| TCP Flag 	| 의미                  	| 목적                                                                 	                |
|----------	|-----------------------	|----------------------------------------------------------------------	                |
| URG      	| 긴급<br>Urgent        	| 중요한 데이터임을 지정한다 <br> 순서에 상관없이 먼저 송신된다                            |
| ACK      	| 승인<br>Acknowledment 	| 패킷 수신 승인을 의미, 이 비트는 접속 요청에 사용되는 SYN 메시지 이후 항상 1로 설정됨 	|
| PSH      	| 푸시<br>Push          	|  버퍼의 내용을 채우지 않고 바로 전송을 수행                                             |
| RST      	| 리셋<br>Reset         	| 연견을 해제하기 위해 사용                                                              |
| SYN      	| 동기화<br>Synchronize 	|  연결 설정에 사용함 <br>연결의 시작 부분에서 순서를 동기화시킴                           |
| FIN      	| 종료<br>Finish        	| 전송할 남은 데이터가 없음을 알린다. 즉 연결종료                                         |

# TCP 수집정보 
| Required information                                                                               | For your system | Example                |
|----------------------------------------------------------------------------------------------------|-----------------|------------------------|
| Type of communication adapter installed in your system (see the instructions following this table) |                 | Ethernet               |
| Resource name                                                                                      |                 | CMN01                  |
| IP address for your system                                                                         |                 | 199.5.83.158           |
| Subnet mask for your system                                                                        |                 | 255.255.255.0          |
| Gateway address                                                                                    |                 | 199.5.83.129           |
| Host name and domain name for your system                                                          |                 | sys400.xyz.company.com |
| IP address for domain name server                                                                  |                 | 199.4.191.76           |

