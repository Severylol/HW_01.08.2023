import os
os.system('cls')
import random

def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def find_indices_in_range(arr, min_value, max_value):
    indices = []
    for i, num in enumerate(arr):
        if min_value <= num <= max_value:
            indices.append(i)
    return indices

if __name__ == "__main__":
    input_list = [1, 5, 88, 100, 2, -4]  # тут можно заменить на generate_random_list(size, min_value, max_value)
    min_value = 33
    max_value = 200

    result = find_indices_in_range(input_list, min_value, max_value)
    print(f"Индексы элементов, принадлежащих диапазону [{min_value}, {max_value}]: {result}")
