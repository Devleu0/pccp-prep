"""이분 탐색 템플릿: lower/upper bound, 파라메트릭 서치."""
from bisect import bisect_left, bisect_right


def count_in_range(sorted_values, lo, hi):
    """정렬된 리스트에서 lo <= x <= hi 인 원소 개수. O(log N)."""
    return bisect_right(sorted_values, hi) - bisect_left(sorted_values, lo)


def min_true(lo, hi, predicate):
    """[lo, hi]에서 predicate(x)가 처음 True가 되는 가장 작은 x를 반환.

    predicate는 단조(False...False True...True)여야 한다. 모두 False면 hi + 1.
    예: 퍼즐 게임 챌린지(최소 숙련도), 입국심사(최소 시간).
    """
    answer = hi + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


def max_true(lo, hi, predicate):
    """[lo, hi]에서 predicate(x)가 True인 가장 큰 x를 반환 (True...True False...False). 없으면 lo - 1.

    예: 징검다리(거리의 최솟값 중 최댓값).
    """
    answer = lo - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer
