def run():
    raw = input("Введите строку: ")
    string = raw.strip()
    if not string:
        print("Ошибка: строка не может быть пустой.")
        return
    if raw != string:
        print("Внимание: введены пробелы по краям, они были убраны.")
    reversed_string = string[::-1]
    word_count = len(string.split())
    print(f"Развёрнутая строка: {reversed_string}")
    print(f"Количество слов: {word_count}")