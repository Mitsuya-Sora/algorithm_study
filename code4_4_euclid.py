# 再帰関数は、ベースケース、処理、再帰呼び出し部分を分けて考える。ベースケースは、何回も呼び出して行って最終的にこれ以上呼び出さない時の返り値
def get_greatest_common_divisor(m: int, n: int) -> int:

    # ベースケース
    if m % n == 0:
        return n

    # 再帰呼び出し
    return get_greatest_common_divisor(n, m % n)


if __name__ == '__main__':
    print(get_greatest_common_divisor(51, 15) == 3)

