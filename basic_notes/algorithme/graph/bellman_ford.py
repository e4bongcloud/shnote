from typing import List, Tuple


def bellman_ford(graph: List[List[Tuple[int, int]]], start: int) -> List[int]:
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # 음수 사이클 검사
    for u in range(n):
        for v, w in graph[u]:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return None
    
    return dist
    
graph = [
    [(1, 10), (3, 5)],
    [(2, 2), (4, 1)],
    [(4, 3)],
    [(0, -1), (2, 6)],
    []
]

start = 0


dist = bellman_ford(graph, start)

if dist is None:
    print("음수 사이클이 존재합니다.")
else:
    print(f"{start}에서 출발한 모든 정점까지의 최단 거리:")
    for i, d in enumerate(dist):
        print(f"{start} -> {i}: {d}")
