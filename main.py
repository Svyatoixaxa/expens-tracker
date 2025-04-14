from tracker import *


def main():
    """Основная функция приложения, реализующая меню.
    Функционал:
    - Добавление новых расходов с валидацией данных
    - Просмотр полного списка расходов
    - Расчет и отображение общей суммы
    - Фильтрация расходов по категориям
    - Завершение работы программы

    Меню:
    1 - Добавить расход
    2 - Показать все расходы
    3 - Показать общую сумму
    4 - Показать расходы по категории
    5 - Выход

    Обрабатываемые исключения:
    - ValueError: при некорректном формате суммы"""
    print("Калькулятор расходов")
    while True:
        print("\nМеню:")
        print("1 - Добавить расход")
        print("2 - Показать все расходы")
        print("3 - Показать общую сумму")
        print("4 - Показать расходы по категории")
        print("5 - Выход")       
        choice = input("Выберите действие: ")
        
        if choice == "1":
            try:
                amount = float(input("Сумма: "))
                category = input("Категория: ").strip()
                description = input("Описание (необязательно): ").strip()
                add_exp(amount, category, description)
                print("Расход добавлен")
            except ValueError as e:
                print(f"Ошибка: {e}")
        
        elif choice == "2":
            if not get_exp():
                print("Нет расходов")
            else:
                for i, exp in enumerate(get_exp(), 1):
                    print(f"{i}. {exp['amount']:.2f} - {exp['category']} ({exp['description']})")
        
        elif choice == "3":
            print(f"Общая сумма: {get_total():.2f}")
        
        elif choice == "4":
            category = input("Введите категорию: ").strip()
            category_expenses = get_category(category)
            if not category_expenses:
                print(f"Нет расходов в категории '{category}'")
            else:
                print(f"Расходы в категории '{category}':")
                for exp in category_expenses:
                    print(f"- {exp['amount']:.2f}: {exp['description']}")
        
        elif choice == "5":
            print("Выход")
            break
        
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()
