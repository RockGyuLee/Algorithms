# This is a sample Python script.

def pibona(n):

    pibonaTemp1 = 0
    pibonaTemp2 = 1
    temp = pibonaTemp1 + pibonaTemp2
    if n == 0:
        return pibonaTemp1
    elif n == 1:
        return pibonaTemp2

    for i in range(3, n + 1):
        pibonaTemp1 = pibonaTemp2
        pibonaTemp2 = temp
        temp = pibonaTemp1 + pibonaTemp2

    return temp

if __name__ == '__main__':

    n = int(input())

    print(pibona(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
