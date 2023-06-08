# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    """
    Функция делит число на указанные числа
    :param arg1: последовательность числе, первое число делимое, остальные - делители
    :return: результат деления
    """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result',
                         [pytest.param(2, 2, 1, marks=pytest.mark.smoke),
                          pytest.param(0, 2, 0, marks=pytest.mark.skip)])
def test_positive_integer(a, b, result):
    """
    Результат - целое число
    """
    assert all_division(a, b) == result
