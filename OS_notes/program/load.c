#include <stdio.h>
#include <time.h>

// loop는 cpu의 점유율은 높아지지만 실질적 연산은 하지않기에 cpu에 부하자체는 가하지 않습니다.
// 정확하게 말하자면은 cpu의 발열이 발생하지 않습니다.  그저 무한하게 반복할 뿐이기 떄문입니다.  
// 따라서 cpu의 로드율이 99%라도 시스템은 정상적으로 동작하는 상황이 됩니다.  
int main(void) {
    do{
        time(NULL);
    } while (1);
    return 0;
}