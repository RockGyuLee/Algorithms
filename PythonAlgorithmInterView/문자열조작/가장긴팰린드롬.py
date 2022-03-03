

def longestPalindrome(self, s: str) -> str:

    def lenPalindrome(left, right) :
        print(left, right)
        while left >= 0 and right <= len(s) -1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)):
        result = max(
            result,
            lenPalindrome(i, i+1),
            lenPalindrome(i, i+2),
            key=len
        )
    return result
if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(None, s))