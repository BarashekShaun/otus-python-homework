"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
        return True


def filter_numbers(nums, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type == ODD:
        return [i for i in nums if i % 2 != 0]
    elif type == EVEN:
        return [i for i in nums if i % 2 == 0]
    elif type == PRIME:
        return [i for i in nums if is_prime(i)]
