from tqdm import tqdm

start = 1 #Начало диапазона
end = 10 #Конец диапазона
step = 2 #Шаг

def run():
    print("Чётные числа от 1 до 10:")
    for i in tqdm(range(start + 1, end + 1, step), desc="Вывод чётных чисел", ncols=100):
        print(i, end=' ')
    print()