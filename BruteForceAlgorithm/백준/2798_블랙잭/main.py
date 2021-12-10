if __name__ == '__main__':

    n, m =input().split(' ')
    arList = input().split(' ')

    arList.sort(reverse=True)

    result = 0
    value = int(m)

    for i in range(int(n)) :
        for j in range(i+1, int(n)) :
            for k in range(j+1, int(n)) :
                if (int(arList[i])+int(arList[j])+int(arList[k])) > value :
                    continue
                else:
                    result = max(result, int(arList[i]) + int(arList[j]) + int(arList[k]))
    print(result)
    # for i in sumList :
    #     sortList.append(int(m) - i)
    # sortList.sort()
    # print(sumList,sortList)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
