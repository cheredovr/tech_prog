def run():
    name = input("Введите ваше имя: ").strip()
    if not name:
        print("Ошибка: имя не может быть пустым.")
    else:
        print(f"Привет, {name}!")