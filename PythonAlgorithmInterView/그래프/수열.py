def permute(self, nums: list[int]) -> list[list[int]]:
    result = []
    prev_list = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_list[:])

        for e in elements :
            next_list = elements[:]
            next_list.remove(e)

            prev_list.append(e)
            dfs(next_list)
            prev_list.pop()


    dfs(nums)

    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    print( permute(None, nums))