zeek는  IDS도 IPS도 아닌 네트워크 트래픽 모니터링 도구이다.

Zeek is not an active security device, like a firewall or intrusion prevention system.  
Rather, Zeek sits on a “sensor,” a hardware, software, virtual, or cloud platform that quietly and unobtrusively observes network traffic.  
Zeek interprets what it sees and creates compact, high-fidelity transaction logs, file content, and fully customized output, suitable for manual review on disk or in a more analyst-friendly tool like a security and information event management (SIEM) system.



grafana:  로그 검색 및 필터링을 위한 Kibana.

kibana: 경고, 그래프 및 대시보드용 Grafana.


Suricata는 알려진 위협에 대한 트래픽을 모니터링하고 감지되면 경고를 생성하는 데 Zeek보다 훨씬 효율적입니다. 
또 다른 이점은 새로운 위협 인텔리전스가 Suricata와 호환되는 형식으로 먼저 제공되는 경우가 많다는 것입니다.

Zeek는 포괄적인 네트워크 트래픽 가시성 및 컨텍스트를 제공하고 네트워크 기준 설정, 
호스트 및 서비스 프로파일링, 수동 인벤토리 수집, 정책 시행, 이상 탐지 및 위협 추적 노력을 지원하는 데 필요한 대량의 고품질 데이터를 제공합니다.

