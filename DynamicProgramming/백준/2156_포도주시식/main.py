def totalScore( scoreList):
    dp = [0] * n
    if n == 1:
        dp[0] = scoreList[0]
    elif n == 2:
        dp[0] = scoreList[0]
        dp[1] = scoreList[0] + scoreList[1]
    else:
        dp[0] = scoreList[0]
        dp[1] = scoreList[0] + scoreList[1]
        dp[2] = max(dp[1], scoreList[2] + scoreList[0], scoreList[2] + scoreList[1])

    for i in range(3, n):
        dp[i] = max( dp[i-1], scoreList[i] + scoreList[i-1] + dp[i-3], scoreList[i] + dp[i-2] )

    return max(dp)



if __name__ == '__main__':
    n = int(input())

    wineScore = []

    for _ in range(n):
       wineScore.append(int(input()))

    print(totalScore(wineScore))
"""

6
6
10
13
9
8
1

9
6
10
13
9
8
1
1
2
4
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
