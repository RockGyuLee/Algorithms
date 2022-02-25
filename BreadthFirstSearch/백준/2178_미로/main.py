from collections import deque

def findRoadMiro(gr, start) :

    moveX = [0,1,0,-1]
    moveY = [1,0,-1,0]

    queue = deque([start])
    while queue :
        v = queue.popleft()
        for i in range(4) :
            x = v[0] + moveX[i]
            y = v[1] + moveY[i]
            if isCheck(x,y):
                if gr[x][y] == 1 :
                    gr[x][y] += gr[v[0]][v[1]]
                    queue.append([x,y])

def isCheck(x,y) :
    if 0 <= x < n and 0 <= y < m :
        return True
    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n,m = map(int,input().split(" "))
    graph = []

    for _ in range(n):
        ar = list(map(int,input()))
        graph.append(ar)
    print(graph)
    findRoadMiro(graph,[0,0])
    print(graph[n-1][m-1])
"""
3 3
100
111
101
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
