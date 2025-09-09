from tqdm import tqdm

def run():
    try:
        num = int(input("Введите число для подсчёта факториала: ").strip())
        if num < 0:
            print("Ошибка: факториал отрицательного числа не определён.")
            return
        if num > 20:
            print("Ошибка: число слишком большое, введите число до 20.")
            return
        factorial = 1
        for i in tqdm(range(1, num + 1), desc="Вычисление факториала", ncols=100):
            factorial *= i
        print(f"Факториал {num}: {factorial}")
    except ValueError:
        print("Ошибка: введите целое число.")