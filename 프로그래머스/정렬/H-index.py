def is_even(index, arr):
    result = []
    for i in arr :
        if index <= i :
            result.append(i)

    return len(result) if index <= len(result) else -1


def solution(citations):
    citations.sort()
    length = max(citations)
    newArr = []
    # print(citations)

    for i in range(length +1) :
        # print(i, citations)
        temp = is_even(i,citations)
        if temp > 0 : newArr.append(temp)

    return len(newArr)-1

if __name__ == '__main__':
    print(solution([0, 1, 2]))
    print(solution([0, 1, 1]))