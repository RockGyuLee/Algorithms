if __name__ == '__main__':

    n = int(input())

    arr = []
    dp = []
    for _ in range(n) :
        arr.append(int(input()))
    if n >= 3 :
        dp.append(arr[0])
        dp.append( max(arr[0]+arr[1] , arr[1]))
        dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
        for i in range(3, n) :
            dp.append(max( arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2] ) )

    elif n == 2 :
        dp.append(max(arr[0]+ arr[1], arr[1]))
    else :
        dp.append(arr[0])

    print(dp.pop())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
