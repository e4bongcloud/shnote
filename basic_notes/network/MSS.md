# MSS(Maximum Segment Size)
MSS (Maximum Segment Size)는 TCP(Transmission Control Protocol) 세그먼트의 최대 크기를 나타내는 값입니다. TCP는 인터넷 상에서 데이터를 안정적으로 전송하기 위한 프로토콜로, 데이터를 일정 크기의 세그먼트로 분할하여 전송합니다.

MSS 값은 TCP 연결을 설정하는 과정에서 상대방과 협상되며, 양쪽 호스트가 통신 가능한 가장 큰 세그먼트 크기를 결정합니다. MSS 값은 TCP 헤더에 포함되어 전송되며, 이를 기반으로 수신 호스트는 세그먼트를 재조립합니다.

MSS 값은 일반적으로 MTU (Maximum Transmission Unit) 값보다 작게 설정됩니다. MTU는 네트워크 상에서 전송 가능한 최대 패킷 크기를 나타내는 값으로, MSS 값은 MTU보다 작아야 한 패킷이 조립될 수 있습니다. MTU 값이 큰 경우에는 큰 패킷을 전송할 수 있지만, 패킷 손실이나 재전송이 발생할 가능성이 높아집니다.

따라서, 적절한 MSS 값을 설정하면 TCP 통신의 안정성과 효율성을 높일 수 있습니다. 일반적으로 MSS 값은 1460 bytes로 설정됩니다. 이는 Ethernet 네트워크에서 사용되는 MTU 값인 1500 bytes에서 TCP 헤더 크기(20 bytes)와 IP 헤더 크기(20 bytes)를 뺀 값입니다.

