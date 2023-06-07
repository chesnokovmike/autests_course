# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_positive_integer():
    """
    Результат - целое число
    """
    assert all_division(4, 2) == 2


@pytest.mark.smoke
def test_positive_float():
    """
    Результат - дробное число
    """
    assert all_division(5, 2) == 2.5


@pytest.mark.acceptance
def test_zero_division():
    """
    Деление на 0
    """
    try:
        all_division(1, 0)
    except ZeroDivisionError:
        print('На ноль делить нельзя')


def test_letter_division():
    """
    Делитель - строка
    """
    try:
        all_division(5, 'a')
    except TypeError:
        print("Нельзя делить на букву")


def test_letter_division_devider():
    """
    Делимое - строка
    """
    try:
        all_division('a', 5)
    except TypeError:
        print('Нельзя разделить букву')