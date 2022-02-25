def solution(sizes):

    max_w_list = []
    max_h_list = []

    for size in sizes:
        if size[0] > size[1] :
            max_w_list.append(size[0])
            max_h_list.append(size[1])
        else :
            max_w_list.append(size[1])
            max_h_list.append(size[0])

    return max(max_w_list) * max(max_h_list)

if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133