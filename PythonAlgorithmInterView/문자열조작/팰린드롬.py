import re
import collections


# 락의 해결방안.
def rock_solution(str) -> bool:
    reg_str_list = re.findall('[a-zA-Z]', str);

    str1 = ''.join(reg_str_list).upper()
    reg_str_list.reverse()
    str2 = ''.join(reg_str_list).upper()

    return str1 == str2


# 상길북에서의 해결방안.
def real_solution(s) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# optimization 된 기능
def optimization_soultion( s: str) -> bool:
    strs = collections.deque()

    for char in s :
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

if __name__ == '__main__':
    print(optimization_soultion("A man, a plan, a canal: Panama"))
    # print(real_solution("race a car"))
