import re

#6-3+5+6-8
#55-50+40
#50+50-100+100-100-100
if __name__ == '__main__':
    stringAr = input().split('-')
    result = 0
    for item in stringAr.pop(0).split('+') :
        result += int(item)

    for item in stringAr :
        sum = 0
        for iitem in item.split('+') :
            sum += int(iitem)
        result -= sum
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
