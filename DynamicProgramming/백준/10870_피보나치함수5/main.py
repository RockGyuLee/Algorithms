
def fibonacci(n) :

    if n == 0 :
        dp[n] = 0
        return 0
    if n == 1 :
        dp[n] = 1
        return 1

    if dp[n] != -1 :
        return dp[n]
    else :
        dp[n] = fibonacci(n -1) + fibonacci(n -2)
        return dp[n]
if __name__ == '__main__':
    n = int(input())
    dp = [ -1 for _ in range(n+1)]
    print(fibonacci(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
