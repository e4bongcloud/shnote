# Delayed-Binding
DDoS (Distributed Denial of Service) 공격에서 Delayed Binding이란, 공격자가 대량의 요청을 보내면서 웹 서버나 네트워크 장비 등이 응답을 처리하는데 많은 자원을 소모하는 상황에서, 응답 처리 속도가 늦어져서 발생하는 현상을 의미합니다.

이러한 공격에서는 다수의 소스에서 대량의 요청을 보내기 때문에, 이를 처리하는 대상 시스템에서 응답 처리 속도가 느려질 수 있습니다. 이러한 상황에서 요청을 처리하는데 걸리는 시간이 길어지면, 시스템 자원이 부족해져서 정상적인 서비스를 제공할 수 없게 되며, 이는 서비스 거부 (Denial of Service) 공격으로 이어질 수 있습니다.

이렇게 Delayed Binding이 DDoS 공격과 연관되는 이유는, 공격자가 대량의 요청을 보내면서 시스템에서 응답을 처리하는데 많은 자원을 소모하기 때문입니다. 따라서 이를 방어하기 위해서는, 서버나 네트워크 장비에서 요청을 처리하는 과정을 최적화하고, 이상한 패턴을 감지하는 방어 메커니즘을 도입하는 등의 방법을 사용해야 합니다.
