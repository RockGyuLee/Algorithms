if __name__ == '__main__':

    n = int(input())
    numbeers = list(map(int, input().split(" ")))
    dp = [];

    dp.append(numbeers[0])

    for i in range(1, len(numbeers)) :
        dp.append(max(numbeers[i], numbeers[i] + dp[i-1]))

    print(max(dp))
"""
10
10 -4 3 1 5 6 -35 12 21 -1
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
