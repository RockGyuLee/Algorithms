from collections import deque

def bfs(graph, start, visited ):

    queue = deque([start])

    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False] * 9

    bfs(graph, 1, visited)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
