# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test():
    # Здесь пишем код
    # весь код я написал в conftest.py
    print(test.pytestmark[0])
    pass
