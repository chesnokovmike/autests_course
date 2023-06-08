# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.mark.usefixtures('write_time_class_fixture')
class TestTask4:

    def test_1(self):
        """
        Болванка теста
        """
        time.sleep(1)
        pass

    def test_2(self, write_time_test_fixture):
        """
        Болванка теста (с фикстурой)
        :param write_time_test_fixture:
        """
        time.sleep(1)

