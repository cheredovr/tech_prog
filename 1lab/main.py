import what_is_name
import twonumb
import strok
import chet
import facktorial
import fibanachi


def main():
    while True:
        print("\nВыберите программу для запуска:")
        print("1. Приветствие по имени")
        print("2. Операции с двумя числами")
        print("3. Операции со строкой")
        print("4. Вывод чётных чисел от 1 до 10")
        print("5. Подсчёт факториала")
        print("6. Найти N-ое число Фибоначчи")
        print("0. Выход")

        choice = input("Введите номер программы: ").strip()

        if choice == '1':
            what_is_name.run()
        elif choice == '2':
            twonumb.run()
        elif choice == '3':
            strok.run()
        elif choice == '4':
            chet.run()
        elif choice == '5':
            facktorial.run()
        elif choice == '6':
            fibanachi.run()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Введите число от 0 до 6.")


if __name__ == "__main__":
    main()