# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    C = int(input())

    for _ in range(C):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]

        for i in range(1,n):
            for j in range(i+1):
                if j == 0 :
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i :
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

        print(max(triangle[n-1]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
2
4
1
1 1
1 1 1
1 1 1 1
4
9
5 7
1 3 2
3 5 5 6

1
4
1
1 1
1 1 1
1 1 1 1
"""