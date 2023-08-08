import os
os.system('cls')
def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ошибка! Пожалуйста, введи число.")


def fill_arithmetic_progression():
    a1 = input_number("Введи первый элемент прогрессии: ")
    d = input_number("Введи разность прогрессии: ")
    n = int(input_number("Введи количество элементов прогрессии: "))

    progression = [a1 + (i * d) for i in range(n)]
    return progression


if __name__ == "__main__":
    result = fill_arithmetic_progression()
    print("Элементы арифметической прогрессии:")
    for num in result:
        print(num)
