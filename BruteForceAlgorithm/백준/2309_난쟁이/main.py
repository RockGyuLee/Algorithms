
if __name__ == '__main__':
    person = []
    for _ in range(9) :
        person.append(int(input()))
    person.sort()

    for i in range(len(person)) :
        for j in range(i+1,len(person)) :
            result = []
            result.append(person[i])
            result.append(person[j])

            if (sum(person) - sum(result)) == 100:
                person.remove(result[0])
                person.remove(result[1])

                for k in person :
                    print(k)
                break

    # print(person)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
