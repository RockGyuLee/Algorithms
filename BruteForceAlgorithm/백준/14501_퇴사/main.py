def maxPrice(day, sum) :

    if day > n :
        return 0

    temp = sum

    #재귀함수 짜는 법을 다시 좀 생각해봐야 겠다. 감이 안잡힌다.
    for i in range(day, n) :
       temp = max(temp, maxPrice(i + tp[i][0], sum + tp[i][1]))
    return temp

if __name__ == '__main__':
    n = int(input())
    dp = [-1 for _ in range(n)]
    tp = []
    for _ in range(n) :
        tp.append(list(map(int,input().split(' '))))
    print(maxPrice(0, 0))
