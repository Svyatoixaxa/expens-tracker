expenses = []

def add_exp(amount: float, category: str, description: str = ""):
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
    """Возвращает список всех расходов."""
    return expenses.copy()

def get_total():
    """Возвращает общую сумму всех расходов."""
    return sum(item['amount'] for item in expenses)

def get_category(category):
    """Возвращает расходы указанной категории."""
    filtered_expenses = []
    category_lower = category.lower()
    
    #Фильтр расходов по категориям
    for item in expenses:
        if item['category'].lower() == category_lower:
            filtered_expenses.append(item)
    
    return filtered_expenses

def reset_exp():
    """Очищает список расходов."""
    expenses.clear()
