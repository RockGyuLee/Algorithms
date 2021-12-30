
def filterMembers(mem) :
    size = len(mem)
    count = 0

    minValue = 100000

    for i in range(size) :
        if minValue > mem[i][1] :
            count += 1
            minValue = mem[i][1]
    return count
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input())
    memberList = []
    for _ in range(n):
        m = int(input())
        arList = []
        for _ in range(m):
            arList.append(list(map(int, input().split(" "))))

        arList.sort()

        a = arList[0][1]
        cnt = 0
        for i in arList:
            if i == arList[0]:
                cnt += 1
            elif i[1] < a:
                cnt += 1
                a = i[1]
        print(cnt)
"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
