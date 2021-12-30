
def jump(y,x):
    if y >= m or x >= m : return 0
    if y == m -1 and x == m-1 : return 1

    print(dp[y][x])

    ret = dp[y][x]

    if dp[y][x] != -1 : return dp[y][x]

    jumpSize = ar[y][x]
    dp[y][x] = jump( y + jumpSize, x) or jump(y, x + jumpSize)
    return dp[y][x]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        m = int(input())
        ar = []
        dp = [[-1] * m for _ in range(m)]
        for _ in range(m):
            ar.append(list(map(int, input().split(" "))))

        print("YES" if jump(0, 0) else "NO")

"""
2
7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 2
3 3 1 2 3 4 1
1 5 2 9 4 7 0
7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 3
3 3 1 2 3 4 1
1 5 2 9 4 7 0
"""


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
