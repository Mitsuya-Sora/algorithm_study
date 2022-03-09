from typing import List
import sys


def bellman_ford_v1(vertices_num: int, single_start: int, path: List[List[int]]) -> None:
    inf = sys.maxsize

    shortest_distances = [inf] * vertices_num
    shortest_distances[single_start] = 0

    for i in range(vertices_num):
        is_changed = False
        for start, end, distance in path:
            if shortest_distances[start] == inf:
                continue
            if shortest_distances[start] + distance < shortest_distances[end]:
                # vertices_num(頂点の数)以上処理を行なっていたら、負のサイクルをもつ事を報告
                if i + 1 == vertices_num:
                    print('NEGATIVE CYCLE')
                    return
                shortest_distances[end] = shortest_distances[start] + distance
                is_changed = True
            else:
                continue

        # そのiの時更新されなければ、終了しているのでループを抜ける
        if not is_changed:
            break
    print(shortest_distances)


if __name__ == '__main__':
    bellman_ford_v1(4, 0, [[0, 1, 2], [0, 2, 3], [1, 2, -5], [1, 3, 1], [2, 3, 2]])
    # [0, 2, -3, -1]
    bellman_ford_v1(4, 0, [[0, 1, 2], [0, 2, 3], [1, 2, -5], [1, 3, 1], [2, 3, 2], [3, 1, 1]])
    # NEGATIVE CIRCLE

