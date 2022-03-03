import collections

# rock solution
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

    dict = collections.defaultdict(list)

    for str in strs :
        str_list = list(str)
        str_list.sort()
        dict[''.join(str_list)].append(str)
        dict[''.join(str_list)].sort()

    return list(dict.values())

# sang solution
def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:

    dict = collections.defaultdict(list)

    for str in strs :
        dict[''.join(sorted(str))].append(str)

    return list(dict.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(groupAnagrams1(None, strs))

    max()
