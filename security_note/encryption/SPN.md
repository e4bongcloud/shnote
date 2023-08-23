# (Substitution-Permutation Network)  


대칭키 암호화에서 많이 사용되는 블록 암호화 구조입니다.

SPN은 대부분의 블록 암호화 알고리즘에서 사용되는 구조로, 먼저 입력 블록을 초기 전치(Initial Permutation)를 이용해 변경하고, 다음으로 Substitution과 Permutation 과정을 반복적으로 수행하여 암호화합니다. 
 
 Substitution 과정에서는 입력 블록을 대체하는 S-Box를 이용해 암호화를 수행하며, Permutation 과정에서는 위치를 바꾸는 P-Box를 이용해 블록을 섞습니다. 마지막으로, 최종 전치(Final Permutation)를 이용해 암호문을 생성합니다.

# 주요 특징
* 여러 개의 함수를 중첩하면 개별 함수로 이루어진 암호보다 안전하다는 Shannon의 이론에 근거
* Substitution Cipher와 Permutation Cipher를 중첩하는 행태로 개발한 암호
* 입력을 여러 개의 소블록으로 나누고 각 소블록을 S-Box에서 대치시키고 그 결과를 다시 P-Box를 전치하는 과정을 반복함

![SPN](https://upload.wikimedia.org/wikipedia/commons/c/cd/SubstitutionPermutationNetwork2.png)

