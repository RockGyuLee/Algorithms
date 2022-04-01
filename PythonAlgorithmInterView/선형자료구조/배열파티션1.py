def arrayPairSum(self, nums: list[int]) -> int:

    min_arr = []
    sum = 0
    nums.sort()


    for i in range(len(nums)):

        min_arr.append(nums[i])

        if len(min_arr) == 2 :
            sum += min(min_arr)
            min_arr = []

    print(sum)




if __name__ == '__main__':
    nums = [6,2,6,5,1,2]

    print(arrayPairSum(None, nums))
