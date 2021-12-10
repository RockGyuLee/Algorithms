
if __name__ == '__main__':
    dp = [ 0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 2
    n = int(input())

    for i in range(3,n+1) :
        dp[i] = (dp[i - 1] + dp[i-2]) % 10007
    print(dp[n])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
