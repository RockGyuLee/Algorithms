def findMovieName(number) :

    count = 0
    defaultNumber = 0

    while True :
        if count == number :
            return defaultNumber -1

        if "666" in str(defaultNumber) :
            count += 1

        defaultNumber += 1

if __name__ == '__main__':
    n = int(input())
    print(findMovieName(n))
