"""가중치 그래프 템플릿: 다익스트라, 플로이드-워셜."""
import heapq

INF = float("inf")


def build_graph(n, edges, directed=False):
    """1-indexed 인접 리스트. edges: (u, v, w) 목록."""
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph


def dijkstra(graph, source):
    """source에서 모든 정점까지 최단 거리 리스트. O((V+E) log V). 음수 간선 불가."""
    dist = [INF] * len(graph)
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def floyd_warshall(n, edges, directed=False):
    """모든 쌍 최단 거리 (1-indexed). O(N^3)이므로 N <= 200~500 정도에서만 쓴다."""
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        if not directed:
            dist[v][u] = min(dist[v][u], w)
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    return dist
