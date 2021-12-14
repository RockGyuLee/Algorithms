
def getMaxWeight() :
    loop.sort()
    ar = []
    nn = n
    for i in range(n) :
        ar.append(loop[i] * nn)
        nn -= 1

    return max(ar)

if __name__ == '__main__':

    n = int(input())
    loop = []
    for _ in range(n) :
      loop.append(int(input()))

    print(getMaxWeight())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
2
10
15

5
100
80
60
40
20

4
10
50
40
50

"""