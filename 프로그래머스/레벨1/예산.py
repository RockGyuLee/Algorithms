
def solution(d, budget):

    d.sort()
    totalP = 0
    count = 0

    for i in d :
        if totalP + i > budget :
            break
        totalP += i;
        count += 1

    return count
if __name__ == '__main__':


    print(solution( [1, 3, 2, 5, 4], 9))
    print(solution([2, 2, 3, 3], 10))