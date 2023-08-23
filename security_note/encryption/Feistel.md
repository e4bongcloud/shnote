#  Feistel
입력 블록을 두 개로 나눈 후, 반복적으로 동일한 함수를 적용해 블록을 섞습니다.  
함수의 입력값은 이전 단계에서 만들어진 블록의 절반과 키이며, 함수의 출력값은 다음 단계의 블록 절반을 결정합니다. 이렇게 블록을 반복적으로 섞으면서 최종 블록을 생성하고, 최종 전치를 이용해 암호문을 생성합니다. Feistel 구조는 SPN과 달리 블록을 섞는 과정에서 XOR 연산을 이용하기 때문에 하드웨어 구현이 용이하며, 블록 크기와 상관없이 사용이 가능합니다.

![Feistel](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Feistel_cipher_diagram_en.svg/330px-Feistel_cipher_diagram_en.svg.png)
