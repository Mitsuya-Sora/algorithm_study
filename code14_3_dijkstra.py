import sys
from typing import Optional, List



class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    @staticmethod
    def parent_index(index: int) -> int:
        return index // 2

    @staticmethod
    def left_child_index(index: int) -> int:
        return 2 * index

    @staticmethod
    def right_child_index(index: int) -> int:
        return (2 * index) + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value):
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def min_child_index(self, index: int) -> int:
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if (self.heap[self.left_child_index(index)] <
               self.heap[self.right_child_index(index)]):
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            min_child_index = self.min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)
        return root


def dijkstra(vertices_num: int, start: int, path: List[List[int]]) -> None:
    used = [False] * vertices_num
    inf = sys.maxsize
    distances = [inf] * vertices_num
    distances[start] = 0
    for i in range(vertices_num):
        min_distance = inf
        min_distance_vertex = -1

        # 残った頂点から、現時点で最短のdistanceを探す
        for vertex in range(vertices_num):
            if not used[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_distance_vertex = vertex

        # -1のままと言うことは、全てused[vertex]がtrueになって処理が残っていないと言うことなのでbreak
        if min_distance_vertex == -1:
            break

        #
        for parent, child, distance in path:
            if parent == min_distance_vertex:
                distances[child] = min([distances[child], distances[min_distance_vertex] + distance])
        used[min_distance_vertex] = True

    print(distances)
    print(used)



if __name__ == '__main__':
    # min_heap = MiniHeap()
    # min_heap.push(5)
    # min_heap.push(6)
    # min_heap.push(2)
    # min_heap.push(9)
    # min_heap.push(13)
    # min_heap.push(11)
    # min_heap.push(1)
    # print(min_heap.heap)
    # # [-9223372036854775807, 1, 6, 2, 9, 13, 11, 5]
    # print(min_heap.pop())
    # # 1
    # print(min_heap.heap)
    # # [-9223372036854775807, 2, 6, 5, 9, 13, 11]
    dijkstra(4, 0, [[0, 1, 2], [0, 2, 3], [1, 2, -5], [1, 3, 1], [2, 3, 2]])
    # [0, 2, -3, -1]
    dijkstra(4, 0, [[0, 1, 1], [0, 2, 4], [1, 2, 2], [1, 3, 5], [2, 1, 1], [2, 3, 1]])
    # [0, 1, 3, 4]
    dijkstra(9, 0, [[0, 1, 4], [1, 0, 4], [0, 6, 7], [6, 0, 7], [1, 6, 11], [6, 1, 11], [1, 7, 20], [7, 1, 20], [1, 2, 9],
                    [2, 3, 6], [2, 4, 2], [3, 4, 10], [3, 5, 5], [4, 5, 15], [4, 7, 1], [4, 8, 5], [5, 8, 12], [6, 7, 1],
                    [7, 8, 3], [2, 1, 9], [3, 2, 6], [4, 2, 2], [4, 3, 10],
                    [5, 3, 5], [5, 4, 15], [7, 4, 1], [8, 4, 5], [8, 5, 12], [7, 6, 1], [8, 7, 3]])
# [0, 4, 11, 17, 9, 22, 7, 8, 11]
