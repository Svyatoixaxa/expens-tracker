""" Модуль тестов для калькулятора расходов.
Проверяет корректность работы всех функций из модуля tracker"""
import pytest
from tracker import *

def test_add_expense():
    """Тестирование добавления нового расхода
    Проверяет:
    - Корректное добавление записи в список расходов
    - Правильность сохранения всех полей (amount, category, description)
    - Соответствие типа данных для суммы (float)"""
    reset_exp()
    add_exp(100.50, "Еда", "Обед")
    assert len(get_exp()) == 1
    assert get_exp()[0]['amount'] == 100.50
    assert get_exp()[0]['category'] == "Еда"
    assert get_exp()[0]['description'] == "Обед"

def test_add_expense_validation():
    """Тестирование валидации входных данных при добавлении расхода
    Проверяет:
    - Отклонение отрицательных сумм
    - Отклонение пустых категорий
    - Тип выбрасываемого исключения (ValueError)"""
    reset_exp()
    with pytest.raises(ValueError):
        add_exp(-100, "Транспорт")
    with pytest.raises(ValueError):
        add_exp(100, "")

def test_get_total():
    """Тестирование расчета общей суммы расходов
    Проверяет:
    - Корректность суммирования нескольких расходов
    - Возвращаемый тип данных (float)
    - Обработку пустого списка расходов (через reset_exp()"""
    reset_exp()
    add_exp(100, "Еда")
    add_exp(200, "Транспорт")
    assert get_total() == 300

def test_get_by_category():
    """Тестирование фильтрации расходов по категории
    Проверяет:
    - Корректность фильтрации по полному совпадению категории
    - Возвращаемую структуру данных
    - Подсчет суммы отфильтрованных записей"""
    reset_exp()
    add_exp(100, "Еда", "Обед")
    add_exp(200, "Еда", "Ужин")
    add_exp(150, "Транспорт")
    result = get_category("Еда")
    assert len(result) == 2
    assert sum(e['amount'] for e in result) == 300

def test_empty_expenses():
    """Тестирование поведения функций с пустым списком расходов
    Проверяет:
    - Поведение get_exp() при отсутствии данных
    - Поведение get_total() при отсутствии данных
    - Поведение get_category() при отсутствии данных"""
    reset_exp()
    assert len(get_exp()) == 0
    assert get_total() == 0
    assert len(get_category("Еда")) == 0
