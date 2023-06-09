import pytest
from pathlib import Path
import datetime
import sys

data_path = Path('test_file.txt')


@pytest.fixture(scope='class')
def write_time_class_fixture():
    """
    Фикстура класса, записывает в файл время начала и время окончания выполнения класса
    """
    with open(data_path, 'a+', encoding='utf-8') as file:
        file.write(f'\nВремя начала выполнения класса {datetime.datetime.now().strftime("%d.%m %H:%M:%S")}')
        yield write_time_class_fixture
        file.write(f"\nВремя окончания выполнения класса {datetime.datetime.now().strftime('%d.%m %H:%M:%S')}")


@pytest.fixture
def write_time_test_fixture():
    """
    Фикстура теста, записывает время выполнения теста
    """
    with open(data_path, 'a+', encoding='utf-8') as file:
        start_time = datetime.datetime.now()
        yield write_time_test_fixture
        finish_time = datetime.datetime.now()
        time_delta = finish_time - start_time
        file.write(f'Время выполнения теста {time_delta}')


# def pytest_runtest_setup(item):  # задание со звездочкой
#     """
#     Метод выводит на печать значения маркера id_check
#     :param item:
#     """
#     for mark in item.iter_markers(name="id_check"):
#         print("id_check аргументы:{}".format(mark.args))
#         sys.stdout.flush()