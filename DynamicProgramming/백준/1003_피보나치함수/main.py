# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = int(input())
    maxNum = -1
    arr = []

    for i in range( n ) :
        qu = int(input())
        arr.append(qu)
        maxNum = max( maxNum, qu)
    dpZero = [0 for i in range(maxNum+1)]
    dpFirst = [0 for i in range(maxNum+1)]

    for i in range( maxNum + 1):
        if i == 0 :
            dpZero[i] = dpZero[i] + 1
        elif i == 1 :
            dpFirst[i] = dpFirst[i] + 1
        else :
            dpZero[i] = dpZero[i -1 ] + dpZero[ i -2]
            dpFirst[i] = dpFirst[i -1] + dpFirst[i -2]

    for i in range(len(arr)) :
        index = arr[i]
        print(dpZero[index], dpFirst[index])

    # print(dpZero,dpFirst)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
