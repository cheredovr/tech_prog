from tqdm import tqdm

MIN_N = 0          # минимально допустимое N
MAX_N = 100        # максимально допустимое N
FIB_START_A = 0    # первое число Фибоначчи
FIB_START_B = 1    # второе число Фибоначчи

def fib(n):
    if n <= 1:
        return n
    a, b = FIB_START_A, FIB_START_B
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
        if n < MIN_N:
            print("Ошибка: номер числа Фибоначчи не может быть отрицательным.")
            return
        if n > MAX_N:
            print(f"Ошибка: число слишком большое, введите число до {MAX_N}.")
            return
        result = fib(n)
        print(f"Число Фибоначчи для N={n}: {result}")
    except ValueError as e:
        print(f"Ошибка: введите целое число. (Подробности: {str(e)})")