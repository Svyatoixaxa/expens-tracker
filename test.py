import pytest
from tracker import *

def test_add_expense():
    reset_exp()
    add_exp(100.50, "Еда", "Обед")
    assert len(get_exp()) == 1
    assert get_exp()[0]['amount'] == 100.50
    assert get_exp()[0]['category'] == "Еда"
    assert get_exp()[0]['description'] == "Обед"

def test_add_expense_validation():
    reset_exp()
    with pytest.raises(ValueError):
        add_exp(-100, "Транспорт")
    with pytest.raises(ValueError):
        add_exp(100, "")

def test_get_total():
    reset_exp()
    add_exp(100, "Еда")
    add_exp(200, "Транспорт")
    assert get_total() == 300

def test_get_by_category():
    reset_exp()
    add_exp(100, "Еда", "Обед")
    add_exp(200, "Еда", "Ужин")
    add_exp(150, "Транспорт")
    result = get_category("Еда")
    assert len(result) == 2
    assert sum(e['amount'] for e in result) == 300

def test_empty_expenses():
    reset_exp()
    assert len(get_exp()) == 0
    assert get_total() == 0
    assert len(get_category("Еда")) == 0
