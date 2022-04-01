
# rock solution brutefoce 방식으로 문제 해결 시간 복잡도는 n제곱이 걸린다.
def twoSum(self, nums: list[int], target: int) -> list[int]:

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target :
                return [i, j]

# 상길북에서 보여준 n제곱이지만 첫번째 얻은 값을 빼고 in 조건으로 값 파악을 하면 ms의 차이는 확연히 들어난다.
def twoSum2(self, nums: list[int], target: int) -> list[int]:
    for i, n  in enumerate(nums):

        element = target - n

        if element in nums[ i+1:]:
            return [i, nums[i+1:].index(element)+ i + 1]

# 시간 복잡도를 생각하여 n의 시간 복잡도만 가지게 변경할 수 있다. object를 활용하여 데이터 추가.
def twoSum3(self, nums: list[int], target: int) -> list[int]:

    nums_map = {}

    # index의 값을 알아야하기 때문에 value에 index값을 넣어준다.
    for i, n  in enumerate(nums):
        nums_map[n] = i

    print(nums_map)

    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - n] :
            return [i, nums_map[target - n]]



if __name__ == '__main__':
    # nums = [3,2,4]
    # target = 6
    nums = [2,5,5,11]
    target = 10
    print(twoSum3(None, nums, target))