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


@pytest.mark.zero
@pytest.mark.smoke
@pytest.mark.acceptance
def test_zero():
    assert all_division(0, 1, 2, 3) == 0


@pytest.mark.smoke
def test_positive():
    assert all_division(15, 5, 2, 1) == 1.5


@pytest.mark.zero
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 2, 0, 3)


def test_type_error():
    with pytest.raises(TypeError):
        all_division(1, '2', 3, 4)


def test_index_error():
    with pytest.raises(IndexError):
        all_division()
