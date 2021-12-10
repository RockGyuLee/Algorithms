def ones(v):
    return v + v;

def Numbeerth_place(v):
    value = v

    for i in range(0,len(str(v))) :
        value = value + int(str(v)[i])
    return value

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    testCount = 20
    maxCount = 10001
    array = [i for i in range(1,10001)]
    copyArray = array[:]
    setA = set([])

    # 내자신 더하고 맨 앞자리에서 하나씩 줄이기.
    for i in array:
        if i < 10 :
            setA.add(ones(i))
        else :
            setA.add(Numbeerth_place(i))

    for i in range(len(setA)):
        result = setA.pop()
        if result > 10000 :
            break
        copyArray.remove(result)

    for i in copyArray :
        print(i)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
