if __name__ == '__main__':
    n = int(input())
    dp = [[] for _ in range(n)]
    arList = []

    for _ in range(n):
       arList.append(list(map(int,input().split(" "))))

    dp[0].append(arList[0][0])
    for i in range(1,len(arList)):
        for j in range( len(arList[i])):
            v = arList[i]
            if j == 0:
                dp[i].append( v[j] + dp[i-1][0])
            elif j == len(v)-1 :
                dp[i].append((v[j] +dp[i-1][len(dp[i-1])-1]))
            else :
                dp[i].append(max(v[j]+dp[i-1][j-1], v[j]+dp[i-1][j]))

    print(max(dp[len(dp)-1]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
