expenses = []

def add_exp(amount: float, category: str, description: str = ""):
    """Добавляет новый расход в систему.
    Параметры:
        - amount (float): Сумма расхода. Должна быть положительным числом.
        - category (str): Категория расхода (например, "Еда", "Транспорт"). Не может быть пустой строкой.
        - description (str, optional): Детали расхода. По умолчанию "".
    Возвращает:
        None: Функция ничего не возвращает.
    Исключения:
        ValueError: Вызывается, если:
            - amount не является положительным числом
            - category пустая строк"""
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    if not category.strip():
        raise ValueError("Категория не может быть пустой")
    
    expenses.append({
        'amount': amount,
        'category': category,
        'description': description
    })

expenses = []

def get_exp():
    """Возвращает полный список всех расходов:
        list[dict]: Список словарей, каждый словарь содержит:
            - 'amount' (float): сумма
            - 'category' (str): категория
            - 'description' (str): описание"""
    return expenses.copy()
def get_total():
    """Вычисляет общую сумму всех расходов
    Возвращает:
        - float: Сумма всех расходов. 0.0 если список пуст."""
    return sum(item['amount'] for item in expenses)

def get_category(category):
    """Фильтрует расходы по указанной категории
    Параметры: category (str): Категория для поиска (например, "Еда")."""
    filtered_expenses = []
    category_lower = category.lower()
    
    #Фильтр расходов по категориям
    for item in expenses:
        if item['category'].lower() == category_lower:
            filtered_expenses.append(item)
    
    return filtered_expenses

def reset_exp():
    """Сбрасывает все данные о расходах.
    Удаляет все внесённые расходы без возможности восстановления
    """
    expenses.clear()
