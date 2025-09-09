def run():
    string = input("Введите строку: ").strip()
    if not string:
        print("Ошибка: строка не может быть пустой.")
        return
    reversed_string = string[::-1]
    word_count = len(string.split())
    print(f"Развёрнутая строка: {reversed_string}")
    print(f"Количество слов: {word_count}")