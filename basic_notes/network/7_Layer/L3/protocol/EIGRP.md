# EIGRP(Enhanced Interior Gateway Routing Protocol)
VLSM과 같은 새로운 네트워크 기술을 지원하지 못하기 떄문에 시스코에서 IGRP를 확장하여 개발한 프로토콜입니다.
EIGRP는 거리 벡터(Distance Vector)와 링크 상태(Link State) 라우팅 프로토콜의 기능을 결합한 하이브리드 라우팅 프로토콜입니다.

EIGRP는 네트워크의 라우팅 경로를 결정하는 데 사용되며, 경로 결정에는 대역폭, 지연, 신뢰성, 로드 밸런싱 등 다양한 요소를 고려합니다. 또한 EIGRP는 목적지까지의 경로에 대한 정보를 라우터 간에 공유하여, 라우팅 테이블을 최신 상태로 유지합니다.

EIGRP는 다양한 기능과 옵션을 제공하여, 대규모 네트워크에서도 빠르고 효율적인 라우팅을 수행할 수 있습니다. 또한, EIGRP는 Cisco 장비에서만 사용 가능한 프로토콜이기 때문에, Cisco 네트워크에서 주로 사용됩니다.

# 특징
1. 수렴속도가 빠르며, 부분적인 갱신을 지원하기 떄문에 적은 대역폭을 필요로합니다.
2. `VLSM`을 지원하며, `DUAL(Diffusing-Update Algorithm)` 알고리즘을 이용하여 네트워크 구성의 변화가 생겼을 때 패킷의 손실 없이 재 라우팅이 가능하다.

# VLSM(Variable LEngth Subnet mask)
어떤 네트워크에서 다양한 길이의 subnet mask를 사용함

# DUAL(Diffusing-Update Algorithm)
전체적인 경로계산에서 루프-방지 기능을 제공하는 EIGRP의 수렴 알고리즘입니다.

