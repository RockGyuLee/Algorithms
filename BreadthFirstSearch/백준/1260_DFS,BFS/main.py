from collections import deque

def bfs(gr, start, visited) :
    queue = deque([start])

    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v, end=" ")
        for i in gr[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True
    print("")

def dfs(gr, start, visited) :

    visited[start] = True
    print(start, end=" ")

    for i in gr[start]:
        if not visited[i] :
            dfs(gr,i,visited)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n, m, v = map(int,(input().split(' ')))

    graph = [[] for _ in range(n+1) ]

    visited = [False] * (n + 1 )
    visited[0] = True
    for _ in range(m) :
        i , j = map(int,input().split(' '))

        graph[i].append(j)
        graph[j].append(i)
    for i in range(len(graph)) :
        graph[i].sort()

    dfs(graph, v, visited)
    print()
    visited[0] = True

    visited = [False] * (n + 1)

    bfs(graph, v, visited)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
