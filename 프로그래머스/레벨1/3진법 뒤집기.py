def mod(v) :
    value = v
    text = ''
    while value > 0 :
        text += str(value % 3)
        value = value // 3
    return text

def solution(n):
    return int(mod(n),3)

if __name__ == '__main__':
    print(solution(45))