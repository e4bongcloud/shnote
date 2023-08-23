# API(Application Programing Interface)

한 프로그램에서 다른 프로그램으로 데이터를 주고받는 방법

ex) 

    내가 메뉴판 음식을 주문함 <- API GET
    음식이 옴 <- API Request
    이게 API

## REST(Representational State Transfer) API

* 인터넷을 통해 정보를 안전하게 교환하기위한 API
* REST라는 아키텍쳐를 적용해 만든 방식이다.
* 간단하게 REST 아키텍쳐를 따른 API = REST API

## REST란?

* REST란 인터넷 통신을 관리하기위한 지침을 만든 구조

# api 접근 종류
* public
    * 누구나 사용가능한 공개 API
* private API
    * 사내에서 쓰는 API
* partner API
    * 미리 정해둔 사람들끼리 쓰는 API

# api 예

* WindowsAPI
* database 관리프로그램 api
* Crimail IP 웹사이트의 OSINT API


# rest와 SOAP의 차이

1. 아키텍처 스타일의 차이: REST는 Representational State Transfer의 약어로, 분산 하이퍼미디어 시스템을 구축하기 위한 아키텍처 스타일입니다. SOAP은 Simple Object Access Protocol의 약어로, 객체 기반의 웹 서비스를 구현하기 위한 프로토콜입니다.
2. 메시지 포맷의 차이: REST는 주로 JSON이나 XML을 이용하여 데이터를 전송합니다. SOAP은 XML을 이용하여 메시지를 전송하며, 보안 및 에러 처리와 같은 추가적인 기능을 제공합니다.
3. 서비스 검색 방법의 차이: REST는 HTTP GET 메서드를 이용하여 서비스의 URI를 통해 검색하며, 이를 통해 REST API의 디자인이 단순하고 직관적입니다. SOAP은 UDDI (Universal Description, Discovery, and Integration)와 같은 별도의 서비스 디렉토리를 이용하여 서비스를 검색합니다.
4. 캐싱의 가능성: REST는 HTTP 프로토콜 자체에서 제공하는 캐싱 기능을 이용할 수 있으며, 이를 통해 네트워크 대역폭을 줄일 수 있습니다. SOAP은 HTTP 프로토콜의 캐싱 기능을 이용할 수 없으므로, 별도의 캐시 서버를 구축해야 합니다.

요약하면, REST와 SOAP은 각각 다른 아키텍처 스타일과 메시지 포맷, 검색 방법, 캐싱 기능 등을 가지고 있습니다. REST는 단순하고 유연한 API를 구현하는 데 적합하며, SOAP은 보안과 에러 처리와 같은 기능을 제공하는 객체 지향적인 웹 서비스를 구현하는 데 적합합니다.