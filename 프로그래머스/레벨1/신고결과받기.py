def solution(id_list, report, k):
    answer = []

    user_list = []
    sum_list = []

    for i in range(0, len(id_list)) :
        sum_list.append(0)
        user_list.append([])
        answer.append(0)

    newReport = list(set(report))

    for i in newReport :
        i1, i2 = i.split(' ')
        user_list[id_list.index(i1)].append(i2)
        sum_list[id_list.index(i2)] += 1

    for i in range(0,len(sum_list)) :
        if sum_list[i] >= k :
            for j in range(0,len(user_list)) :
                stop_user = user_list[j]
                if stop_user.count(id_list[i]) != 0 :
                    answer[j] += 1

    return answer

if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
    print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"], 3))
