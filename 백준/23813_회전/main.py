if __name__ == '__main__':
    n = input()
    strN = list(n)

    result = 0

    while True :
        text = strN.pop(-1)
        strN.insert(0,text)

        compareValue = ''.join(strN)
        if n == compareValue :
            result += int(compareValue)
            break

        result += int(compareValue)

    print(result)

#12345


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
