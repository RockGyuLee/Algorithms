from collections import deque

def getFindVirus(gr, start, linkNetWork):
    # print(gr)
    queue = deque(gr[start])
    linkNetWork[start] = True
    newList = []
    while queue :
        v = queue.popleft()
        linkNetWork[v] = True
        for i in gr[v]:
            if not linkNetWork[i] :
                queue.append(i)


    for i in linkNetWork:
        if i :
            newList.append(i)
    # print(newList,linkNetWork)
    return len(newList) - 2

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = [ [] for _ in range(n+1)]
    linkedNetwork = [False for _ in range(n + 1)]
    linkedNetwork[0] = True
    for i in range(1,m+1):
        net1, net2 = map(int, input().split(" "))
        graph[net1].append(net2)
        graph[net2].append(net1)

    print(getFindVirus(graph, 1, linkedNetwork))
"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
2
1 2
3 4
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
