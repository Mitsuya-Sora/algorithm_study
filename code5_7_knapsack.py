from typing import List

# N個の品物のi番目の重さはweight[i],価値はvalue[i]。重さがmax_wightを超えず、最大価値になるように品物を選ぶ。


def knapsack(n: int, max_weight: int,
             value: List[int], weight: List[int]) -> int:
    # max_value[i][w]重さがwを超えず、i番目までの品物での最大価値。
    # インデックス番号なので、箱は+1個作らなければいけない
    # max_value[i]としてただi番目でやろうと思ったが、できない場合はもう少し粒度を上げる。
    max_value = [[0] * (max_weight + 1) for j in range(n + 1)]
    # ちなみにこう定義すると、不具合起きる
    # max_value = [[0] * (max_weight + 1)] * (n + 1)

    for i in range(n):
        for j in range(max_weight + 1):

            if j - weight[i] >= 0:
                max_value[i + 1][j] = max([max_value[i + 1][j],
                                           max_value[i][j - weight[i]] + value[i]])

            max_value[i + 1][j] = max([max_value[i][j],
                                       max_value[i + 1][j]])
            
        
        print(max_value[i+1])

    return max_value[n][max_weight]


def knapsack_v2(n: int, max_weight: int,
                value: List[int], weight: List[int]) -> int:

    N, W = map(int, input().split())

    # 各メニューの料金と幸せさを入力
    wv = [list(map(int, input().split())) for _ in range(N)]

    # 最大化問題なのでdpテーブルを0で初期化
    # dp[i][j]は、料金の合計j以下という制約下でi番目までのメニューから任意のメニューを選んだ場合の幸せさの最大値
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # メニューi+1を選ばない場合で仮更新してから、メニューi+1個目を選べる場合は再更新
    for i, (w, v) in enumerate(wv):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]
            if j - w >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)


if __name__ == "__main__":
    print(knapsack(6, 65, [120, 130, 80, 100, 250, 185],
                   [10, 12, 7, 9, 21, 16]))
    # 745
    # print(knapsack(11, 5000, [10, 6, 10, 10, 22, 17, 23, 37, 20, 33, 36],
    #                [750, 700, 900, 600, 1200, 1250, 1850, 2050, 1750,
    #                 2700, 3150]))
    # 770
    print(knapsack(3, 7, [1, 10, 5], [1, 4, 3]))
    # 15
    print(knapsack(3, 7, [10, 5, 1], [1, 4, 3]))
    # 15
    print(knapsack(3, 7, [5, 10, 1], [1, 4, 3]))
    # 15
    print(knapsack(3, 7, [1, 5, 10], [1, 4, 3]))
    # 15
    print(knapsack(3, 5, [1, 2, 4], [2, 2, 3]))
    # 6
