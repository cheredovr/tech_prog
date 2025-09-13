import name
import two_numbers
import string_ops
import chet
import factorial
import fibonacci

# Словарь программ: "название": функция
PROGRAMS = {
    "Приветствие по имени": name.run,
    "Операции с двумя числами": two_numbers.run,
    "Операции со строкой": string_ops.run,
    "Вывод чётных чисел от 1 до 10": chet.run,
    "Подсчёт факториала": factorial.run,
    "Найти N-ое число Фибоначчи": fibonacci.run,
}

EXIT_TEXT = "Выход"

def main():
    while True:
        print("\nВыберите программу для запуска:")

        menu_items = list(PROGRAMS.keys()) + [EXIT_TEXT]
        for idx, item in enumerate(menu_items, start=1):
            print(f"{idx}. {item}")

        choice = input("Введите номер программы: ").strip()

        if not choice.isdigit():
            print(f"Неверный выбор. Введите число от 1 до {len(menu_items)}.")
            continue

        choice_num = int(choice)
        if 1 <= choice_num <= len(PROGRAMS):
            # Получаем функцию через ключ
            program_name = menu_items[choice_num - 1]
            PROGRAMS[program_name]()
        elif choice_num == len(menu_items):
            print("Выход из программы.")
            break
        else:
            print(f"Неверный выбор. Введите число от 1 до {len(menu_items)}.")

if __name__ == "__main__":
    main()
