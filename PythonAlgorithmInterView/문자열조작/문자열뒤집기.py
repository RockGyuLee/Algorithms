
def reverseString(self, s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right :
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def python_reverseString(self, s: list[str]) -> None :
    s.reverse()

def python_reverseString1(self, s:list[str]) -> None :
    s[:] =s[::-1]

if __name__ == '__main__':

    str_list = ["h","e","l","l","o"]
    print(str_list)
    # reverseString(None,str_list)
    #python_reverseString(None,str_list)
    python_reverseString1(None, str_list)
    print(str_list)

