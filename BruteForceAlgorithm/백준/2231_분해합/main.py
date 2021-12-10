if __name__ == '__main__':
    #216
    n = int(input())
    result = 0
    for i in range(1,n+1) :
        sum = 0
        for j in range(len(str(i))) :
           sum += int(str(i)[j])
        if i+ sum == n :
            result = i
            break

    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
#     1
#     3
#     5
#     7
#     9
#     20
#     31
#     42
#     53
#     64
#     9903
#     9914
#     9925
#     9927
#     9938
#     9949
#     9960
#     9971
#     9982
#     9993
# #