# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = input()

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort(reverse=True)

    value = 0;

    for i in range(int(n)) :
        value = value + (int(a[i]) * int(b[i]))


    print(value)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
