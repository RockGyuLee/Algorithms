import numbers


def solution(numbers, hand):

    keyPad = {
        1 : [0,0], 2 : [0,1], 3 : [0,2],
        4 : [1,0], 5 : [1,1], 6 : [1,2],
        7 : [2,0], 8 : [2,1], 9 : [2,2],
        '*' : [3,0], 0 : [3,1], '#' : [3,2]
    }

    location_left_hand = keyPad['*'];
    location_right_hand = keyPad['#'];

    answer = ""

    for i in numbers :
        #왼손인 경우
        if i == 1 or i == 4 or i == 7 :
            location_left_hand = keyPad[i]
            answer = answer + "L"
        #오른손인 경우
        elif i == 3 or i == 6 or i == 9 :
            location_right_hand = keyPad[i]
            answer = answer + "R"
        else :
            a, lH, rH = getPushHand(keyPad[i],location_left_hand, location_right_hand, hand)
            location_left_hand = lH
            location_right_hand = rH
            answer = answer + a

    return answer

def getPushHand(pushKeyPad, leftHand, rightHand, mainHand):
    lH = abs(pushKeyPad[0] - leftHand[0]) + abs(pushKeyPad[1] - leftHand[1])
    rH = abs(pushKeyPad[0] - rightHand[0]) + abs(pushKeyPad[1] - rightHand[1])

    if lH == rH :
        if mainHand == 'left' :
            return "L", pushKeyPad, rightHand
        elif mainHand == 'left' :
            return "R", leftHand, pushKeyPad

    # 왼손이 더 가깝게 움직일 수 있다.
    if lH - rH < 0 :
        return "L", pushKeyPad, rightHand
    else :
        return "R", leftHand, pushKeyPad

    return ""


if __name__ == '__main__':

    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))