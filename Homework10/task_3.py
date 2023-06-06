# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


# @pytest.mark.smoke
# def test_positive_integer():
#     """
#     Результат - целое число
#     """
#     assert all_division(4, 2) == 2


@pytest.mark.parametrize('*arg1', [4, 2, 2])
def test_positive_integer(*arg1):
    """
    Результат - целое число
    """
    assert all_division(*arg1) == 2