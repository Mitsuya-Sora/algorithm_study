# 計算量がクソデカ(アルゴリズムp98を参照)
def fibo_recursive(nth: int) -> int:

    # ベースケース
    if nth == 0:
        return 0
    elif nth == 1:
        return 1

    # 処理と再帰呼び出し
    return fibo_recursive(nth - 1) + fibo_recursive(nth - 2)


def fibo_forloop(nth: int) -> int:

    # 辞書{}にしなければならない、リスト[]にすると、appendでしか入れられない
    sum = {}
    for i in range(nth + 1):
        if i == 0 or i == 1:
            sum[i] = i
        else:
            sum[i] = sum[i - 1] + sum[i - 2]

    return sum[nth]


# eliminate waste of recursive
def fibo_recursive_using_chache(nth: int) -> int:

    cache = {}

    def _fibo(nth: int) -> int:
        # base case
        if nth == 0:
            return 0
        elif nth == 1:
            return 1

        # if cache[nth] is registered before, code does not calculate again, and use cache value.
        if nth in cache:
            return cache[nth]
        
        cache[nth] = _fibo(nth - 1) + _fibo(nth - 2)
        return cache[nth]

    return _fibo(6)


if __name__ == '__main__':
    print(fibo_recursive(6))
    # 8
    print(fibo_forloop(6))
    # 8
    print(fibo_recursive_using_chache(6))
    # 8
