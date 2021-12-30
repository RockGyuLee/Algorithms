def isPrime(value) :

    for i in range(2,value):
        if i == value -1 : return True

        if value % i == 0 : return False


def solution(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)) :
            for k in range(j+1, len(nums)):
                v = nums[i] +nums[j] + nums[k]
                if isPrime(v) : count += 1
    return count
if __name__ == '__main__':
    print(solution([1,2,7,6,4]))
    print(solution([1,2,3,4]))