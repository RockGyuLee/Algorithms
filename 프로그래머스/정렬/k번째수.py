def solution(array, commands):
    answer = []

    for items in commands :
        newArr = array[items[0] -1 : items[1] ]
        newArr.sort()
        answer.append(newArr[items[2] -1])

    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
