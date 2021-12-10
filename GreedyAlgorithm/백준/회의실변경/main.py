# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = input();
    arr = [];
    count = 0
    startTime, endTime = 0, 0
    for i in range(int(n)) :
        s, e = input().split();
        arr.append([int(s),int(e)])

    #입력된 값을 강의가 끝나는 시간에 맞게 sort
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])

    for i in range(len(arr)):
        startTime = arr[i][0]
        if(endTime <= startTime) :
            endTime = arr[i][1]
            count = count + 1
    print(count)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
