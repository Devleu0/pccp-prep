"""유니온 파인드 템플릿과 크루스칼 MST."""


class DisjointSet:
    """경로 압축 + 크기 기준 합치기. 연산 하나에 거의 O(1)."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:  # 경로 압축 (재귀 없이, 재귀 깊이 초과 방지)
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        """합쳤으면 True, 이미 같은 집합이면 False."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def kruskal(n, edges):
    """0-indexed 정점 n개, edges: (u, v, w). MST 총 가중치를 반환 (예: 섬 연결하기)."""
    dsu = DisjointSet(n)
    total = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if dsu.union(u, v):
            total += w
    return total
