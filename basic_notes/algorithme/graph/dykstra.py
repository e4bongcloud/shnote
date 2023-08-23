import numpy as np

def project_onto_set(x, s):
    """
    x를 닫힌 볼록 집합 s에 투영하는 Dykstra 알고리즘을 구현한다.
    """
    # 알고리즘에 사용할 변수 초기화
    y = x.copy()
    z = x.copy()
    max_iters = 1000
    tol = 1e-6
    
    # Dykstra 알고리즘 수행
    for i in range(max_iters):
        y_old = y.copy()
        y = s(y + z - x)
        z = z + y - x
        if np.linalg.norm(y - y_old) < tol:
            break
            
    return y

def project_onto_ball(v, center, radius):
    """
    중심이 center이고 반지름이 radius인 구에 벡터 v를 투영하는 함수
    """
    # 중심으로부터 벡터 v의 거리 계산
    distance = np.linalg.norm(v - center)
    
    # 벡터 v가 구 안에 있으면 그대로 반환
    if distance < radius:
        return v
    
    # 벡터 v가 구 바깥에 있으면 구의 표면에 투영
    else:
        return center + (v - center) * radius / distance

# 투영하고자 하는 벡터와 볼록 집합 설정
v = np.array([1.5, 2.5])
ball_center = np.array([1, 1])
ball_radius = 1

# 볼록 집합 투영 함수를 정의
def project_onto_ball_set(x):
    return project_onto_ball(x, ball_center, ball_radius)

# 투영 실행
projected_v = project_onto_set(v, project_onto_ball_set)

print("v:", v)
print("투영된 v:", projected_v)
