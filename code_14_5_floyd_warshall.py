from typing import List
import sys


def floyd_warshall(vertices_num: int,path: List[List[int]]) -> None:

    min_distances = [[sys.maxsize] * vertices_num for _ in range(vertices_num)]
    for n in range(vertices_num):
        min_distances[n][n] = 0

    for start, stop, distance in path:
        min_distances[start][stop] = distance

    for k in range(vertices_num):
        for j in range(vertices_num):
            for i in range(vertices_num):
                min_distances[i][j] = min([min_distances[i][j], min_distances[i][k] + min_distances[k][j]])

    for v in range(vertices_num):
        if min_distances[v][v] < 0:
            print('exist negative circle')
            return
    else:
        print(min_distances[0])


if __name__ == '__main__':
    floyd_warshall(4, [[0, 1, 2], [0, 2, 3], [1, 2, -5], [1, 3, 1], [2, 3, 2]])
    # [0, 2, -3, -1]
    floyd_warshall(4, [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 5], [2, 1, 1], [2, 3, 1]])
    # [0, 1, 3, 4]
    floyd_warshall(9, [[0, 1, 4], [1, 0, 4], [0, 6, 7], [6, 0, 7], [1, 6, 11], [6, 1, 11], [1, 7, 20], [7, 1, 20],
                       [1, 2, 9], [2, 3, 6], [2, 4, 2], [3, 4, 10], [3, 5, 5], [4, 5, 15], [4, 7, 1], [4, 8, 5],
                       [5, 8, 12], [6, 7, 1], [7, 8, 3], [2, 1, 9], [3, 2, 6], [4, 2, 2], [4, 3, 10], [5, 3, 5],
                       [5, 4, 15], [7, 4, 1], [8, 4, 5], [8, 5, 12], [7, 6, 1], [8, 7, 3]])
    # [0, 4, 11, 17, 9, 22, 7, 8, 11]
