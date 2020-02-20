a = 17
b = [2, 5, 6, 8, 1]


def dp(target, ls):
    dp.max_sum = -float('inf')
    dp.ans = []
    dp.i = 0

    def dp_aux(chose, remain, curr_sum):
        print(dp.i)
        dp.i += 1
        if curr_sum >= target:
            return
        if curr_sum > dp.max_sum:
            dp.max_sum = curr_sum
            dp.ans = chose
        if len(remain) == 0:
            return
        curr_item = [remain[0]]
        dp_aux(chose + curr_item, remain[1:], curr_sum + curr_item[0])
        dp_aux(chose, remain[1:], curr_sum)

    dp_aux([], ls, 0)
    return dp.ans


if __name__ == '__main__':
    print(dp(a, b))
