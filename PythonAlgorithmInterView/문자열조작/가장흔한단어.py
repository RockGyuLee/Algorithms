import collections
import re


def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

    words = []
    para = re.sub('[^\w]',',',paragraph.lower())


    for word in para.split(',') :

        if word != ''  and word not in banned:
            words.append(word)

    dict = collections.defaultdict(int)

    for word in words :
        dict[word] += 1

    return max(dict, key=dict.get)

if __name__ == '__main__':

    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]

    # paragraph = "a."
    # banned = []

    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]

    print(mostCommonWord(None,paragraph,banned))