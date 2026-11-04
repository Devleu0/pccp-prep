"""위상 정렬 템플릿 (Kahn 알고리즘)."""
from collections import deque


def topological_sort(n, edges):
    """0-indexed 정점 n개, edges: (u, v)는 u → v (u가 먼저).

    사이클이 있으면 None, 없으면 위상 순서 리스트를 반환.
    """
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return order if len(order) == n else None
