# def solution(board):
#     answer = 0
#     if len(board) < 2 or len(board[0]) < 2 : return 1;
#
#     for i in range( 1, len(board)) :
#         for j in range( len(board[i])) :
#             if i - 1 < 0 or j - 1 < 0:
#                 continue
#             if board[i][j] == 0 :
#                 continue
#             minValue = min(board[i][j-1], board[i-1][j-1], board[i-1][j])
#             board[i][j] = minValue + 1
#
#             if answer < minValue + 1 :
#                 answer = minValue +1
#     return answer * answer
#
#
# if __name__ == '__main__':
#     print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
#     print(solution([[1],[1]]))

def solution():
    n = int(input())
    s = []
    num = 0
    while n > 0:
        s.append(n % 2)
        n //= 2
    print(s)
    for i in range(len(s)):
        if s[i] == 1:
            num += 3 ** i
    print(num)


if __name__ == '__main__':
    print(solution());
