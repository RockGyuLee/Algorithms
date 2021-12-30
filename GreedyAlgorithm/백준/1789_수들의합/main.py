

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())

    count = 1
    sum = 0

    while True :
        sum += count
        if sum == n :
            print(count)
            break
        elif sum > n :
            print(count -1)
            break
        count += 1



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
