from tqdm import tqdm

def run():
    print("Чётные числа от 1 до 10:")
    for i in tqdm(range(2, 11, 2), desc="Вывод чётных чисел", ncols=100):
        print(i, end=' ')
    print()