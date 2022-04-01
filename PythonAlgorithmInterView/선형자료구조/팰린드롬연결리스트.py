
def isPalindrome(self, head: [list]) -> bool:
    q : list = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop() :
            return False

    return True

    # while left < right :
    #     head.p

if __name__ == '__main__':
    head = [1, 2, 2, 1]

    print(isPalindrome(None, head))