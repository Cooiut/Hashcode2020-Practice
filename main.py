# 读文件
# file = "Test/a_example.in"
file = "Test/b_small.in"
# file = "Test/c_medium.in"
# file = "Test/d_quite_big.in"
# file = "Test/e_also_big.in"

f = open(file, "r")

amount = int(f.readline().split(" ")[0])
denominations = tuple(int(i) for i in f.readline().rstrip().split(" "))

f.close()

# 操作

# min(myList, key=lambda x:abs(x-myNumber))


# Method 1
result = list(denominations)
current_sum = sum(result)
while current_sum > amount:
    # print(result)
    diff = current_sum - amount
    closest = min(result, key=lambda x: abs(x - diff))
    result.remove(closest)
    current_sum = sum(result)

'''# Method 2
result = set(denominations)
current_sum = sum(result)
removed = set()
while current_sum > amount:
    mini = min(result)
    result.remove(mini)
    removed.add(mini)
    current_sum = sum(result)
while current_sum < amount:
    if len(removed) == 0:
        break
    diff = amount - current_sum
    mini = min(removed, key=lambda x: abs(x - diff))
    result.add(mini)
    removed.remove(mini)
    current_sum = sum(result)
while current_sum > amount:
    diff = current_sum - amount
    closest = min(result, key=lambda x: abs(x - diff))
    result.remove(closest)
    current_sum = sum(result)'''
'''
import sys
sys. setrecursionlimit(200000)


from haphai_dp import dp

result = dp(amount, denominations)
'''
# 写文件
if __name__ == '__main__':
    print("Score is: " + str(sum(result)))
    output = [str(denominations.index(i)) for i in sorted(result)]

    f = open(file.replace("in", "out"), "w")
    f.write(str(len(output)) + "\n")
    f.write(" ".join(output))

    f.close()
