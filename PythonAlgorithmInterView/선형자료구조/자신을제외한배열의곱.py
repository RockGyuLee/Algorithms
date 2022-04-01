
#rock 문제 풀이방법. time limit exceeded가 걸린다.
def productExceptSelf(self, nums: list[int]) -> list[int]:

    result = []

    p = 1
    for i in range(len(nums)):
        result.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums), 0, -1):
        result[i-1] *= p
        p *= nums[i-1]

    return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [-1, 1, 0, -3, 3]

    print(productExceptSelf(None, nums))