# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input())
    ar = []
    dp = [1,2,4]

    for i in range(n) :
        ar.append(int(input()))

    maxNum = max(ar)
    for i in range(3,maxNum):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    for i in ar:
        print(dp[i-1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
