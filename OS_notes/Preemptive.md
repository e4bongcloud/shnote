# 선점형(Preemptive)
* 프로세스가 점유한 CPU를 다른 프로세스가 빼앗을 수 있음
* 대화형, 시간 분할, 실시간 시스템에 적당
* 문맥 교환이 많아 오버헤드가 큼
* 대표적 방식: RR(Round Robin), SRT(Shortest Remaining Time), MFQ(Multi level Feedback Queue), MLQ(Mult level Queeue)

# 

# 비선점형(Non-Preemptive)
* 점유자원을 반환할떄까지 선점 불가 

대표적 방식: SJF, FIFO, 우선순위, HRN, 기한부

# FIFO

# SJF(shortest job first)


# HRN
SJF에서 발생하는 기아 현상을 해결하기위해 에이징 기법을 사용하여 활용하는 스케줄링 기법이다.  

대기시간 + 실행시간 / 실행시간 = 우선순위