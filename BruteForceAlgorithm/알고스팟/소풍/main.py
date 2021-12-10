#
def countParings(taken):

    firstFree = -1

    for i in range(len(taken)):
        if not taken[i] :
            firstFree = i
            break
    #기저사례 : 모든 학생이 True면 짝을 찾은 한 가지 방법을 찾았으니 1과 함께 return 한다.
    if firstFree == -1 :
        return 1

    result = 0

    #짝을 찾은 친구는 통과 시켜야한다.
    for i in range(firstFree+1,len(taken)) :
        if not taken[i] and areFriends[firstFree][i] :

            taken[firstFree] = taken[i] = True
            result += countParings(taken)
            taken[firstFree] = taken[i] = False

    return result

if __name__ == '__main__':
    caseNum = int(input())

    for i in range(caseNum) :

        n, m = map(int,input().split())
        taken = [False] * n

        areFriends = [[False for i in range(n)] for i in range(n)]

        friendsList = list(map(int, input().split()))

        for i in range(0,len(friendsList)-1, 2) :
            areFriends[friendsList[i]][friendsList[i+1]] = True
            areFriends[friendsList[i+1]][friendsList[i]] = True

        print(countParings(taken))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
