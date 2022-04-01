
#재귀함수로 로직을 구현.
import collections


def removeDuplicateLetters( s: str) -> str:

    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        if set(s) == set(suffix):
            return char + removeDuplicateLetters( suffix.replace(char,''))
    return ''

#스택으로 로직 구현. 이해가 잘 안되서 몇번을 봐야할거같다.
def removeDuplicateLetters2( s: str) -> str:

    counter, seen, stack = collections.Counter(s), set(), []

    for char in s :
        print(counter, seen, stack, char)
        counter[char] -= 1
        if char in seen :
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0 :
            seen.remove(stack.pop())


        stack.append(char)
        seen.add(char)

    print(counter)

if __name__ == '__main__':
    s = "cbacdcbc"
    print(removeDuplicateLetters2(s))