def is_even(n):
    if isinstance(n, (int, float)) and n.is_integer():
        return "чётное" if int(n) % 2 == 0 else "нечётное"
    return "не целое число"

def parse_number(value: str):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except ValueError:
        raise ValueError("Некорректное число")

def run():
    try:
        num1 = parse_number(input("Введите первое число: "))
        num2 = parse_number(input("Введите второе число: "))

        sum_val = num1 + num2
        avg = sum_val / 2
        quotient = "Деление на ноль невозможно" if num2 == 0 else num1 / num2
        remainder = "Деление на ноль невозможно" if num2 == 0 else num1 % num2

        print(f"Сумма: {sum_val}")
        print(f"Среднее: {avg}")
        print(f"Частное: {quotient}")
        print(f"Остаток: {remainder}")

        print(f"Первое число ({num1}): {is_even(num1)}")
        print(f"Второе число ({num2}): {is_even(num2)}")
        print(f"Сумма ({sum_val}): {is_even(sum_val)}")
        print(f"Среднее ({avg}): {is_even(avg)}")
        if isinstance(quotient, (int, float)):
            print(f"Частное ({quotient}): {is_even(quotient)}")
        if isinstance(remainder, (int, float)):
            print(f"Остаток ({remainder}): {is_even(remainder)}")
    except ValueError:
        print("Ошибка: введите числовые значения.")