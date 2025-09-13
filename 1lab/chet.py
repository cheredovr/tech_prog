from tqdm import tqdm

START = 1   # Начало диапазона
END = 10    # Конец диапазона
STEP = 2    # Шаг

def run():
    print(f"Чётные числа от {START} до {END}:")
    for i in tqdm(range(START + 1, END + 1, STEP), desc="Вывод чётных чисел", ncols=100):
        print(i, end=' ')
    print()