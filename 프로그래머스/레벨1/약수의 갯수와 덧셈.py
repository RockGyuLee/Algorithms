def isCount(value):
    count = 0
    for i in range(1, value +1):
        if value % i == 0 :
            count += 1
    return count
def solution(left, right):
    answer = 0

    for v in range(left, right+1):
        if isCount(v) % 2 == 0 :
            answer += v
        else :
            answer -= v

    return answer

if __name__ == '__main__':
    print(solution(24,27))