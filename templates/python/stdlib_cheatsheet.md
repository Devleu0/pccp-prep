# Python 표준 라이브러리 치트시트 (IDE 없는 환경용)

| 목적 | 코드 |
| --- | --- |
| 개수 세기 | `from collections import Counter; Counter(arr).most_common(k)` |
| 기본값 딕셔너리 | `from collections import defaultdict; g = defaultdict(list)` |
| 덱 | `from collections import deque; q.appendleft(x); q.popleft(); q.rotate(k)` |
| 최소 힙 | `import heapq; heapq.heappush(h, x); heapq.heappop(h); heapq.heapify(arr)` |
| 최대 힙 | 값에 `-`를 붙여 push/pop |
| 이분 탐색 | `from bisect import bisect_left, bisect_right, insort` |
| 순열/조합 | `from itertools import permutations, combinations, product, accumulate` |
| 다중 키 정렬 | `arr.sort(key=lambda x: (-x[1], x[0]))` |
| 메모이제이션 | `from functools import lru_cache` → `@lru_cache(maxsize=None)` |
| 재귀 한도 | `import sys; sys.setrecursionlimit(10**6)` |
| 진법 변환 | `int("1011", 2)`, 10진수를 k진수 문자열로 바꾸는 함수는 직접 작성 |
| 시간 문자열 | `m, s = map(int, "12:34".split(":")); total = m * 60 + s`, `f"{t // 60:02d}:{t % 60:02d}"` |
| 2차원 리스트 | `[[0] * m for _ in range(n)]` (`[[0] * m] * n`은 같은 행을 공유하는 버그) |
| 전치 / 회전 | `list(zip(*grid))`, 시계 방향 90도: `[list(r) for r in zip(*grid[::-1])]` |
