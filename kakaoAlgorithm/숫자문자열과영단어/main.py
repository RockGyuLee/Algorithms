# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def solution(s):
    exchangeWord = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    answer = s;

    for i in range(len(exchangeWord)):
        answer = answer.replace(exchangeWord[i], str(i))
    return int(answer)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution('one4seveneight')

