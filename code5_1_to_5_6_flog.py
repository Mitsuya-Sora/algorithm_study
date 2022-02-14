from typing import List
import sys


# 5.1
def flog_with_dynamic_programming_with_receive(height: List[int]) -> int:
    dp = {}

    for i in range(len(height)):
        if i == 0:
            dp[0] = 0
        elif i == 1:
            dp[1] = abs(height[1] - height[0])
        else:
            one_step_cost = abs(height[i] - height[i - 1])
            two_step_cost = abs(height[i] - height[i - 2])
            dp[i] = min([one_step_cost + dp[i - 1], two_step_cost + dp[i - 2]])

    return dp[len(height) - 1]


# 5.3
def flog_with_dynamic_programming_with_relaxation(height: List[int]) -> int:
    dp = [sys.maxsize] * len(height)

    for i in range(len(height)):
        if i == 0:
            dp[0] = 0
        if i > 0:
            dp[i] = dp[i - 1] + abs(height[i] - height[i - 1])
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + abs(height[i] - height[i - 2]))

    return dp[len(height) - 1]


# code 5.4
def flog_with_dynamic_programming_distribute(height: List[int]) -> int:
    dp = [sys.maxsize] * len(height)

    for i in range(len(height)):
        if i == 0:
            dp[0] = 0
        if i + 1 < len(height):
            dp[i + 1] = min([dp[i + 1], dp[i] + abs(height[i] - height[i + 1])])
        if i + 2 < len(height):
            dp[i + 2] = min([dp[i + 1] + abs(height[i] - height[i + 1]),
                             dp[i] + abs(height[i] - height[i + 2])])

    return dp[len(height) - 1]


# 5.5
def flog_with_recursive(height: List[int]) -> int:

    def _flog_with_recursive(i: int) -> int:
        if i == 0:
            return 0

        candidate = float("inf")

        candidate = min(candidate, _flog_with_recursive(i - 1) +
                        abs(height[i] - height[i - 1]))

        if i > 1:
            candidate = min(candidate, _flog_with_recursive(i - 2) +
                            abs(height[i] - height[i - 2]))

        return candidate

    return _flog_with_recursive(len(height) - 1)


# 5.6
def flog_with_recursive_memo(height: List[int]) -> int:

    cache = {}

    def _flog_with_recursive(i: int) -> int:
        if i == 0:
            return 0

        if i in cache:
            return cache[i]

        candidate = float("inf")

        candidate = min(candidate, _flog_with_recursive(i - 1) +
                        abs(height[i] - height[i - 1]))

        if i > 1:
            candidate = min(candidate, _flog_with_recursive(i - 2) +
                            abs(height[i] - height[i - 2]))

        cache[i] = candidate
        return candidate

    return _flog_with_recursive(len(height) - 1)


if __name__ == '__main__':
    # all will return 8
    heights = [2, 9, 4, 5, 1, 6, 10]
    print(flog_with_dynamic_programming_with_receive(heights))
    print(flog_with_dynamic_programming_with_relaxation(heights))
    print(flog_with_dynamic_programming_distribute(heights))
    print(flog_with_recursive(heights))
    print(flog_with_recursive_memo(heights))
