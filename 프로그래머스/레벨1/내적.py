def solution(a, b):
    n , result = len(a), 0

    for i in range(n):
       result += a[i] * b[i]

    return result

if __name__ == '__main__':
    print(solution([1,2,3,4] , [-3,-1,0,2]))
    print(solution([-1,0,1],	[1,0,-1]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
