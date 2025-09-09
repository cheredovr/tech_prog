from tqdm import tqdm

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
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
        if n < 0:
            print("Ошибка: номер числа Фибоначчи не может быть отрицательным.")
            return
        if n > 100:
            print("Ошибка: число слишком большое, введите число до 100.")
            return
        result = fib(n)
        print(f"Число Фибоначчи для N={n}: {result}")
    except ValueError as e:
        print(f"Ошибка: введите целое число. (Подробности: {str(e)})")