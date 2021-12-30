from collections import deque

def getDanjiNumber(gr, start):

    queue = deque([start])
    moveX = [-1, 0, 1, 0]
    moveY = [0, 1, 0, -1]
    gr[start[0]][start[1]] += 1
    count = 1

    while queue :
        v = queue.popleft()
        for i in range(4):
            x = v[0] + moveX[i]
            y = v[1] + moveY[i]
            if isCheck(x,y) :
                if gr[x][y] == 1:
                    gr[x][y] += 1
                    count += 1
                    queue.append([x,y])
    return count

def isCheck(x,y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    graph = []

    danjiList = []

    for _ in range(n):
        graph.append(list(map(int,input())))

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                danjiList.append(getDanjiNumber(graph,[i,j]))

    danjiList.sort()

    print(len(danjiList))
    for i in danjiList :
        print(i)

    # for i in range(n):
    #     for j in range(n) :
    #         print(graph[i][j], end=" ")
    #     print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
