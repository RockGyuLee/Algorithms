if __name__ == '__main__':

    n = list(input())
    n.sort(reverse=True)

    sum = 0
    for i in n:
        sum += int(i)
    print(sum,n)
    if sum % 3 != 0 or "0" not in n:
        print(-1)
    else:
        print(''.join(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
