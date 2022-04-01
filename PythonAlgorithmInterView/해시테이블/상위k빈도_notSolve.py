import collections


def topKFrequent(self, nums: list[int], k: int) -> list[int]:

    freqs = collections.Counter(nums)
    result = []

    # for i in freqs.keys() :
    #     if freqs[i] >= k:
    #         result.append(i)

    return result

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2

    print(topKFrequent(None, nums, k))