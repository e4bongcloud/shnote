# MTTF(Mean Time To Failure), 

* 신뢰성
    * 시스템의 신뢰성 평가 요소
        * 시스템의 전체 가동률
        * 신뢰성 유지를 위한 경제적 처리 방안
        * 시스템 구성 요소의 신뢰도
* 신뢰성 평가 요소
    * 평균 사용 시간(mtbf : mean time between failure)
    * 평균 수리 시간(mttr : mean time to repair)
    * 평균 고장 시간(mttf : mean time to failures)
    * 신뢰도(reliability, 가용도)

* 신뢰성
    * 신뢰성 평가 요소
    * 평균 사용 시간(mtbf : mean time between failure)

# MTBF 평균 무고장 시간 (Mean Time Between Failure)
mtbf = (사용1+ 사용2 + ... + 사용n) / n

# MTTR 평균수리시간 (mean time to repair)    
mttr = (고장1 + 고장2 + ... + 고장n) / n

# MTTF 평균가동시간 (mean time to failures)
mttf = mtbf + mttr

# 신뢰도(reliability, 가용도)

신뢰도 = MTBF / MTTF
      = MTBF / MTBF + MTTR
