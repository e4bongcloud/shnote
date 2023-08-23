# SET(Secure Electronic Transaction)
인터넷을 통해 안전하게 금융 거래를 수행하기 위한 프로토콜입니다. SET은 1996년 VISA, MasterCard, American Express, Discover 등 글로벌 결제 회사들이 개발했으며, SSL(Secure Sockets Layer)을 기반으로 하고 있습니다.

# 특징 

* 암호화: SET은 거래 데이터를 암호화하여 안전하게 전송합니다. 이를 위해 RSA 공개키 암호화 방식을 사용합니다.
* 인증: SET은 전자상거래 참여자를 인증하는데, 디지털 인증서를 사용합니다. 디지털 인증서는 거래 참여자의 공개키와 신원 정보를 포함합니다.
* 전자서명: SET은 거래를 인증하기 위해 전자서명을 사용합니다. 거래 참여자는 거래 데이터를 전자서명하여 무결성을 보장합니다.
* 취소 기능: SET은 거래 취소 기능을 제공합니다. 거래 취소는 거래 참여자의 동의가 필요하며, 취소 거래는 원래 거래와 동일한 암호화와 인증 절차를 거칩니다.

SET은 전자상거래의 보안성을 높이기 위한 프로토콜로, 신뢰성 있는 거래를 위해 공인인증서와 같은 기술을 사용합니다. 그러나, SET은 인프라 및 인증서 발급 등의 문제로 인해 상용화되지 못하고 있습니다. 현재는 SSL/TLS 등의 프로토콜이 보편화되어 있으며, 결제 카드사들도 EMV 칩 카드와 같은 안전한 결제 수단을 제공하고 있습니다.