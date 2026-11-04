from templates.python.binary_search import count_in_range, max_true, min_true
from templates.python.disjoint_set import DisjointSet, kruskal
from templates.python.graph_search import bfs_grid, label_components
from templates.python.shortest_path import INF, build_graph, dijkstra, floyd_warshall
from templates.python.topological_sort import topological_sort


def test_bfs_grid_shortest_path():
    grid = ["111", "101", "111"]
    assert bfs_grid(grid, (0, 0), (2, 2)) == 5
    assert bfs_grid(["10", "01"], (0, 0), (1, 1)) == -1
    assert bfs_grid(["1"], (0, 0), (0, 0)) == 1


def test_label_components_sizes():
    grid = [
        [1, 1, 0],
        [0, 0, 0],
        [1, 0, 1],
    ]
    label, sizes = label_components(grid)
    assert sorted(sizes.values()) == [1, 1, 2]
    assert label[0][0] == label[0][1] != 0
    assert label[1][1] == 0


def test_binary_search_helpers():
    assert count_in_range([1, 2, 2, 3, 5], 2, 3) == 3
    assert min_true(1, 100, lambda x: x * x >= 50) == 8
    assert min_true(1, 5, lambda x: False) == 6
    assert max_true(1, 100, lambda x: x * x <= 50) == 7
    assert max_true(1, 5, lambda x: False) == 0


def test_dijkstra_and_floyd_agree():
    edges = [(1, 2, 1), (2, 3, 2), (1, 3, 5), (3, 4, 1)]
    dist = dijkstra(build_graph(4, edges), 1)
    assert dist[1:] == [0, 1, 3, 4]
    fw = floyd_warshall(4, edges)
    assert fw[1][1:] == dist[1:]
    assert floyd_warshall(2, [])[1][2] == INF


def test_disjoint_set_and_kruskal():
    dsu = DisjointSet(4)
    assert dsu.union(0, 1)
    assert not dsu.union(1, 0)
    assert dsu.find(0) == dsu.find(1) != dsu.find(2)
    # 프로그래머스 '섬 연결하기' 예제
    assert kruskal(4, [(0, 1, 1), (0, 2, 2), (1, 2, 5), (1, 3, 1), (2, 3, 8)]) == 4


def test_topological_sort():
    order = topological_sort(4, [(0, 1), (1, 2), (0, 3)])
    assert order.index(0) < order.index(1) < order.index(2)
    assert topological_sort(2, [(0, 1), (1, 0)]) is None
