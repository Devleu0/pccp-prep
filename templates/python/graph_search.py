"""격자/그래프 탐색 템플릿: BFS 최단거리, 연결 요소 라벨링.

시험장에서 IDE 없이 그대로 칠 수 있도록 표준 라이브러리만 사용한다.
"""
from collections import deque

DIRECTIONS_4 = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs_grid(grid, start, goal, wall="0"):
    """격자에서 start → goal 최단 이동 칸 수(시작 칸 포함)를 반환. 도달 불가면 -1.

    grid: 문자열 리스트나 2차원 리스트. wall 값과 같은 칸은 지나갈 수 없다.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[0] * cols for _ in range(rows)]
    sr, sc = start
    dist[sr][sc] = 1
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        if (r, c) == tuple(goal):
            return dist[r][c]
        for dr, dc in DIRECTIONS_4:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not dist[nr][nc] and str(grid[nr][nc]) != wall:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return -1


def label_components(grid, land=1):
    """land 값 칸들의 4방향 연결 요소에 번호를 붙인다.

    반환: (label 격자(0 = 미포함), {label: 크기})
    '석유 시추' 같은 덩어리 크기 집계 문제에 쓴다.
    """
    rows, cols = len(grid), len(grid[0])
    label = [[0] * cols for _ in range(rows)]
    sizes = {}
    next_id = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != land or label[i][j]:
                continue
            next_id += 1
            label[i][j] = next_id
            queue = deque([(i, j)])
            size = 0
            while queue:
                r, c = queue.popleft()
                size += 1
                for dr, dc in DIRECTIONS_4:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == land and not label[nr][nc]:
                        label[nr][nc] = next_id
                        queue.append((nr, nc))
            sizes[next_id] = size
    return label, sizes
