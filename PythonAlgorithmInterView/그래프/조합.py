def combine(self, n: int, k: int) -> list[list[int]]:

    result = []

    def dfs(elements, start, k):

        if k == 0 :
            result.append(elements[:])
            return

        for i in range( start , n+1):
            elements.append(i)
            dfs(elements, i +1, k -1)
            elements.pop()

    dfs([], 1, k)

    return result
if __name__ == '__main__':
    n = 4
    k = 2

    combine(None, n,k)