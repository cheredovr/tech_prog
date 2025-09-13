from tqdm import tqdm

MIN_NUM = 0      # минимально допустимое число
MAX_NUM = 20     # максимально допустимое число
START = 1        # начало диапазона факториала

def run():
    try:
        num = int(input("Введите число для подсчёта факториала: ").strip())
        if num < MIN_NUM:
            print("Ошибка: факториал отрицательного числа не определён.")
            return
        if num > MAX_NUM:
            print(f"Ошибка: число слишком большое, введите число до {MAX_NUM}.")
            return
        factorial = 1
        for i in tqdm(range(START, num + 1), desc="Вычисление факториала", ncols=100):
            factorial *= i
        print(f"Факториал {num}: {factorial}")
    except ValueError:
        print("Ошибка: введите целое число.")