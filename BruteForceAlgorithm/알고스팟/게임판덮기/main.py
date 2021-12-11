## 알고스팟 너무 어렵다ㅠㅠ

def covergamepan(gamePan, startIndex) :

    ok = True

    for ele in gamePan :
        for j in ele :
            if j == '.' :
                ok = False

    # 배열속에 .으로 시작된 값이 없으면 모든 case를 찾은것이므로 1를 반환한다.
    if ok == True : return 1;

    for ele in range(len(gamePan)) :
        print(len(str(ele)))


if __name__ == '__main__':
    caseNum = int(input())
    nm = []
    gamePan = []
    for _ in range(caseNum) :
        n, m = map(int,input().split(' '))
        nm.append([n,m])
        playBoard = []
        for _ in range(n) :
            string = str(input())
            playBoard.append(string)
        gamePan.append(playBoard)

    for i in range(len(gamePan)) :
        print(covergamepan(gamePan[i], 0))
"""
1
3 7
#.....#
#.....#
##...##
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
