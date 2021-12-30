
if __name__ == '__main__':

    n = int(input())

    m = list(map(int, input().split(" ")))

    operator = list(map(int, input().split(" ")))
    operatorList = []

    for i in range(len(operator)) :
        if operator[i] :
            for j in range(operator[i]) :
                operatorList.append(i)

    """아직 해결 못했음."""
"""
6
1 2 3 4 5 6
2 1 1 1

3
3 4 5
1 0 1 0
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
