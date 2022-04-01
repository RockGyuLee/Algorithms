def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)

    for index, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:

            last = stack.pop()
            answer[last] = index - last

        stack.append(index)

    return answer

if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(dailyTemperatures(None, temperatures))