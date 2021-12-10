
if __name__ == '__main__':
    # print_hi('PyCharm')

    money = 1000

    price = int(input())

    paybackMoney = money - price
    count = 0

    while True :
        if paybackMoney // 500 != 0 :
            count += paybackMoney // 500
            paybackMoney = paybackMoney % 500
        elif paybackMoney // 100 != 0 :
            count += paybackMoney // 100
            paybackMoney = paybackMoney % 100
        elif paybackMoney // 50 != 0 :
            count += paybackMoney // 50
            paybackMoney = paybackMoney % 50
        elif paybackMoney // 10 != 0 :
            count += paybackMoney // 10
            paybackMoney = paybackMoney % 10
        elif paybackMoney // 5 != 0 :
            count += paybackMoney // 5
            paybackMoney = paybackMoney % 5
        else:
            count += paybackMoney // 1
            paybackMoney = paybackMoney % 1

        if  paybackMoney == 0 :
            break
    print(count)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
