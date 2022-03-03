import collections


def solution(quest_list: list, answer_list: list) -> int:
    deque = collections.deque()

    for item in quest_list[int(answer_list[0]) - 1: int(answer_list[1])]:
        deque.append(int(item))

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return 0
    return 1


def dp_solution(items: list) -> int:
    f, s = items

    return 1 if dp[f - 1][s - 1] else 0


if __name__ == '__main__':
    n = int(input())
    strs = input().split(' ')
    dp = [[0 for _ in range(n)] for _ in range(n)]
    m = input()
    list = []

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if strs[i] == strs[i + 1]:
            dp[i][i + 1] = 1

    for i in range(2, n):
        for j in range(n - i):
            if strs[j] == strs[j + i] and dp[j + 1][j + i - 1] == 1:
                dp[j][j + i] = 1

    for _ in range(int(m)):
        f, s = map(int, input().split(' '))
        list.append([f, s])

    for items in list:
        print(dp_solution(items))
"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
"""
