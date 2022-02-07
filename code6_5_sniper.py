from typing import List


# 二分探索法　binary search
def get_min_penalty_to_sniper(init_heights: List[int], velocities: List[int]) -> int:
    n = len(init_heights)
    height_after_n_second = ([x + y * (n - 1) for (x, y) in zip(init_heights, velocities)])

    left, right = 0, max(height_after_n_second)

    while right - left > 1:
        mid = (right + left) // 2
        can_shot_all = True

        remaining_time = [0] * n
        for i in range(n):
            if init_heights[i] > mid:
                can_shot_all = False
            else:
                remaining_time[i] = (mid - init_heights[i]) // velocities[i]
        sorted(remaining_time)
        for i in range(n):
            if remaining_time[i] < i:
                can_shot_all = False

        if can_shot_all:
            right = mid
        else:
            left = mid

    return right


if __name__ == '__main__':
    h = [1, 3, 8, 12]
    s = [6, 3, 5, 2]
# 0s = 1, 3, 8,12
# 1s = 7, 6,13,14
# 2s =13, 9,18,16
# 3s =19,12,23,18
    print(get_min_penalty_to_sniper(h, s))
