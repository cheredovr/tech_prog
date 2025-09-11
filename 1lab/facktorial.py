from tqdm import tqdm

min_num = 0     # минимально допустимое число
max_num = 20     # максимально допустимое число
start = 1       # начало диапазона факториала

def run():
    try:
        num = int(input("Введите число для подсчёта факториала: ").strip())
        if num < min_num:
            print("Ошибка: факториал отрицательного числа не определён.")
            return
        if num > max_num:
            print("Ошибка: число слишком большое, введите число до 20.")
            return
        factorial = 1
        for i in tqdm(range(start, num + 1), desc="Вычисление факториала", ncols=100):
            factorial *= i
        print(f"Факториал {num}: {factorial}")
    except ValueError:
        print("Ошибка: введите целое число.")