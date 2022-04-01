import collections


def numJewelsInStones(self, jewels: str, stones: str) -> int:

    freqs = collections.defaultdict(int)
    count = 0

    for char in stones :
            freqs[char] += 1

    for char in jewels :
            count += freqs[char]

    return count

if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"

    numJewelsInStones(None, jewels, stones)