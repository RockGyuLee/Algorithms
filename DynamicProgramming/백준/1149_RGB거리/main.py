if __name__ == '__main__':
    n = int(input())
    housePrice = []
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for _ in range(n) :
        housePrice.append(list(map(int, input().split(' '))))

    dp[0][0] = housePrice[0][0]
    dp[0][1] = housePrice[0][1]
    dp[0][2] = housePrice[0][2]

    for i in range(1,len( housePrice)) :
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + housePrice[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + housePrice[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + housePrice[i][2]

        if i == len(housePrice) -1 :
            print(min(dp[i]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
