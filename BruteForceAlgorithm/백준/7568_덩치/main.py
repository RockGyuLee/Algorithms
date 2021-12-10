"""
5
55 185
58 183
88 186
60 175
46 155
"""

# def isHeavy(index,person):
#     if index == len(person) : return



if __name__ == '__main__':
    caseNum = int(input())

    person = []

    for _ in range(caseNum) :
        w, h = input().split(' ')
        person.append({"weight" : w, "height" : h})

    for i in range(len(person)) :
        iW = int(person[i]['weight'])
        iH = int(person[i]['height'])
        rank = 1
        for j in range( len(person)) :
            iiW = int(person[j]['weight'])
            iiH = int(person[j]['height'])
            if iW < iiW and iH < iiH :
                rank += 1
        print(rank, end=' ')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
