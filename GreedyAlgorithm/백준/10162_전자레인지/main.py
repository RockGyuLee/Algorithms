def solution(time):

    button = [0,0,0]
    notZeroTimer = 0
    while True :

        if time == 0 :
            break

        if time // 300:
            button[0] += time // 300
            time = time % 300
        elif time // 60 :
            button[1] += time // 60
            time = time % 60

        elif time // 10:
            button[2] += time //10
            time = time % 10

        else:
            notZeroTimer = -1
            break

    if notZeroTimer == -1 :
        return [notZeroTimer]

    return button

if __name__ == '__main__':

    n = int(input())

    ar = solution(n)

    for i in ar :
        print(i, end=' ')

    # print(100 // 300)
"""
버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
