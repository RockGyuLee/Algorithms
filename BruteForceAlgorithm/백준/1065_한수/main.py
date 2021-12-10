# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputNum = input()
    hansu = 0
    for i in range(1,int(inputNum)+1) :
        if i < 100 :
            hansu = hansu + 1
        elif int(str(i)[1]) -  int(str(i)[0]) ==  int(str(i)[2]) -  int(str(i)[1]) :
            hansu = hansu + 1

    print(hansu)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
