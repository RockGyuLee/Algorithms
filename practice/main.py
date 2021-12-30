# def matrixmult(a, b) :
#
#     n = len(a)
#     c = [ [0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 c[i][j] += a[i][k] * b[k][j]
#                 print(c)
#
#     return c

#
# def fibonachi(n):
#     print(n)
#     if n <= 1:
#         return n
#
#     return fibonachi(n - 1) + fibonachi( n - 2)
#

def dpFibo(n):

    dp = [-1] * (n +1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n + 1):
        dp[i] = dp[i -2] + dp[i -1]

    print(dp)
    return dp[n]

def forLoopfibo(dp, n) :

    if dp[n] != -1 : return dp[n]

    if n <= 1 :
        dp[n] = n
        return dp[n]

    dp[n] = forLoopfibo(dp, n-2) + forLoopfibo(dp,n-1)

    return dp[n]

def notListUseFibo(n):

    zeroVari = 0
    oneVari = 1

    for i in range(2, n+1):
        temp = zeroVari + oneVari
        print(zeroVari, oneVari, temp)
        zeroVari = oneVari
        oneVari = temp


    return oneVari
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    testA = [
        [2,3],
        [4,1]
    ]
    testB = [
        [5,7],
        [6,8]
    ]
    # print(matrixmult(testA,testB))

    # print(fibonachi(30))

    # print(dpFibo(100))
    #
    # dp = [-1] * 51
    # print(forLoopfibo(dp,50))

    print(notListUseFibo(10))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
