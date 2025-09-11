from tqdm import tqdm

min_n = 0          # минимально допустимое N
max_n = 100        # максимально допустимое N
fib_start_a = 0    # первое число Фибоначчи
fib_start_b = 1    # второе число Фибоначчи

def fib(n):
    if n <= 1:
        return n
    a, b = fib_start_a, fib_start_b
    for _ in tqdm(range(n - 1), desc="Вычисление числа Фибоначчи", ncols=100):
        a, b = b, a + b
    return b

def run():
    try:
        user_input = input("Введите номер числа Фибоначчи (N): ").strip()
        print(f"DEBUG: Полученный ввод: '{user_input}'")  # Debugging line
        if not user_input:
            print("Ошибка: ввод не может быть пустым.")
            return
        n = int(user_input)
        if n < min_n:
            print("Ошибка: номер числа Фибоначчи не может быть отрицательным.")
            return
        if n > max_n:
            print(f"Ошибка: число слишком большое, введите число до {max_n}.")
            return
        result = fib(n)
        print(f"Число Фибоначчи для N={n}: {result}")
    except ValueError as e:
        print(f"Ошибка: введите целое число. (Подробности: {str(e)})")